from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from allauth.account.decorators import verified_email_required
from django.contrib import messages
from home.models import Policy, CompanySocialMedia
from order.models import *
from userprofile.models import UserDetail, UserAddress
import razorpay
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import hmac
import hashlib 
import binascii
from shop.settings.current import razorpay_key_id, razorpay_key_secret, DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

r_key_id = razorpay_key_id
r_key_secret = razorpay_key_secret

@login_required(login_url='account_login')
def cart(request):
    current_user = request.user
    
    cart = Cart.objects.filter(user_id=current_user.id)
    
    total = 0
    for prod in cart:
        if prod.product.discount_price:
            total += prod.product.discount_price * prod.quantity
        else:
            total += prod.product.price * prod.quantity
    
    context = {'cart': cart, 'total': total, }
    return render(request, "order/cart.html", context)
    


@login_required(login_url='account_login')
def add_to_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    product= Product.objects.get(id=id)
    
    checkinproduct = Cart.objects.filter(product_id=id, user_id=current_user.id)
    
    if checkinproduct:
        control = 1
    else:
        control = 0
    
    if control == 1:
        data = Cart.objects.get(product_id=id, user_id=current_user.id)
        data.quantity += 1
        data.save()
    else:
        data = Cart()
        data.user_id = current_user.id
        data.product_id = id
        data.quantity = 1
        data.save()
    messages.success(request, "Product added to Cart")
    return HttpResponseRedirect(url)
    


@login_required(login_url='account_login')
def minus_to_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    cartItem = Cart.objects.get(id=id, user_id=current_user.id)
    
    if cartItem.quantity == 1:
        cartItem.delete()
        messages.success(request, "Your item deleted form Cart.")
        return redirect('cart')
    else:
        data = Cart.objects.get(id=id, user_id=current_user.id)
        data.quantity -= 1
        data.save()
    messages.success(request, "Product Quantity Changed to Cart")
    return HttpResponseRedirect(url)
    


@login_required(login_url='account_login')
def delete_from_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    Cart.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted form Cart.")
    return HttpResponseRedirect(url)
    


@login_required(login_url='account_login')
def place_order(request):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    cart = Cart.objects.filter(user_id=current_user.id)
    form = OrderForm()
    userdetail = UserDetail.objects.get(user_id=current_user.id)
    useraddress = UserAddress.objects.get(user_id=current_user.id)
    total = 0
    context = {}

    if cart.count() == 0:
        return redirect("order_completed_cart")

    else:
        for prod in cart:
            if prod.product.discount_price:
                total += prod.product.discount_price * prod.quantity
            else:
                total += prod.product.price * prod.quantity
        
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                data = Order()
                data.first_name = form.cleaned_data['first_name']
                data.last_name = form.cleaned_data['last_name']
                data.email = form.cleaned_data['email']
                data.phone = form.cleaned_data['phone']
                data.address_line_1 = form.cleaned_data['address_line_1']
                data.address_line_2 = form.cleaned_data['address_line_2']
                data.pincode = form.cleaned_data['pincode']
                data.city = form.cleaned_data['city']
                data.state = form.cleaned_data['state']
                data.note = form.cleaned_data['note']
                data.user_id = current_user.id
                data.total = total
                data.ip = request.META.get('REMOTE_ADDR')
                data.save()

                totalAmount = int(total * 100)
                client = razorpay.Client(auth=(r_key_id, r_key_secret))
                r_payment = client.order.create({"amount": totalAmount, "currency": "INR", "payment_capture": "1"})
                context.update({'r_payment': r_payment, })

                data.payment_txnid = r_payment['id']
                data.save()
                
                for rs in cart:
                    detail = OrderProduct()
                    detail.order_id = data.id
                    detail.product_id = rs.product_id
                    detail.user_id = current_user.id
                    detail.quantity = rs.quantity
                    if rs.product.discount_price:
                        detail.price = rs.product.discount_price
                    else:
                        detail.price = rs.product.price
                    detail.save()
                
            else:
                messages.error(request, form.errors)
                return HttpResponseRedirect(url)
    
        context.update({'cart': cart, 'total': total, 'form': form, 'userdetail': userdetail, 'useraddress': useraddress, "r_key_id": r_key_id, })
        return render(request, "order/place_order.html", context)
    

@csrf_protect
@csrf_exempt
@login_required(login_url='account_login')
def order_completed_cart(request):
    current_user = request.user
    order = Order.objects.filter(user_id=current_user.id).last()
    ordered_products = OrderProduct.objects.filter(order_id = order.id)

    if request.method == 'POST':
        a = request.POST
        order.razorpay_payment_id = a['razorpay_payment_id']
        order.razorpay_signature = a['razorpay_signature']
        order.save()
    else:
        return redirect("order_failed_cart")

    if order.razorpay_payment_id and order.razorpay_signature:
        message_conc = order.payment_txnid + "|" + order.razorpay_payment_id

        def create_sha256_signature(key, message):
            key = key.encode()
            message = message.encode()
            return hmac.new(key, message, hashlib.sha256).hexdigest()

        generated_signature = create_sha256_signature(r_key_secret, message_conc)
        if (generated_signature == order.razorpay_signature):
            order.payment_done = True
            order.save()
            Cart.objects.filter(user_id=current_user.id).delete()
            
            for rs in ordered_products:
                product = Product.objects.get(id=rs.product_id)
                product.quantity_on_stock -= rs.quantity
                product.save()

            plain_text = get_template('order/email/order_confirmed.txt')
            rendered_html = get_template('order/email/order_confirmed.html')
            context_data = {'order': order, 'ordered_products': ordered_products, }
            email_subject = "Your Order is Confirmed"
            from_email = DEFAULT_FROM_EMAIL
            to_email = request.user.email
            text_content = plain_text.render(context_data)
            html_content = rendered_html.render(context_data)
            email = EmailMultiAlternatives(email_subject, text_content, from_email, [to_email])
            email.attach_alternative(html_content, "text/html")
            email.send()

    else:
        order.status = 'Failed'
        order.save()
        return redirect("order_failed_cart")

    messages.success(request, "Your Order has been Successfully Completed. Thank You.")
    return render(request, "order/order_completed.html", {"order": order, "ordered_products": ordered_products, })



@login_required(login_url='account_login')
def order_failed_cart(request):
    messages.error(request, "Your Order is Failed. Please Try Again.")
    return render(request, "order/order_failed.html")



@login_required(login_url='account_login')
def buy_now(request, id, slug, sku):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    form = OrderForm()
    product = Product.objects.get(id=id)
    userdetail = UserDetail.objects.get(user_id=current_user.id)
    useraddress = UserAddress.objects.get(user_id=current_user.id)
    total = 0
    context = {}
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        form2 = QuantityForm(request.POST)
        if form.is_valid() and form2.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.pincode = form.cleaned_data['pincode']
            data.city = form.cleaned_data['city']
            data.state = form.cleaned_data['state']
            data.note = form.cleaned_data['note']
            data.user_id = current_user.id
            data.ip = request.META.get('REMOTE_ADDR')
            
            detail = OrderProduct()
            detail.product_id = product.id
            detail.quantity = form2.cleaned_data['quantity']
            
            if product.discount_price:
                detail.price = product.discount_price
            else:
                detail.price = product.price

            if detail.quantity <= 0:
                messages.error(request, "Quantity must be atleast One.")
                return HttpResponseRedirect(url)
            else:
                if product.discount_price:
                    total += product.discount_price * detail.quantity
                else:
                    total += product.price * detail.quantity
                data.total = total
                data.save()

                totalAmount = int(total * 100)
                client = razorpay.Client(auth=(r_key_id, r_key_secret))
                r_payment = client.order.create({"amount": totalAmount, "currency": "INR", "payment_capture": "1"})
                context.update({'r_payment': r_payment, })

                data.payment_txnid = r_payment['id']
                data.save()
                
                detail.order_id = data.id
                detail.user_id = current_user.id
                detail.save()
                
            
        else:
            messages.error(request, "Enter All Fields Correctly.")
            return HttpResponseRedirect(url)
        
    
    context.update({'product': product, 'total': total, 'form': form, 'userdetail': userdetail, 'useraddress': useraddress, "r_key_id": r_key_id })
    return render(request, "order/buy_now.html", context)
    

@csrf_protect
@csrf_exempt
@login_required(login_url='account_login')
def order_completed_now(request):
    current_user = request.user
    order = Order.objects.filter(user_id=current_user.id).last()
    ordered_products = OrderProduct.objects.filter(order_id = order.id)

    if request.method == 'POST':
        a = request.POST
        order.razorpay_payment_id = a['razorpay_payment_id']
        order.razorpay_signature = a['razorpay_signature']
        order.save()
        if order.razorpay_payment_id and order.razorpay_signature:
            message_conc = order.payment_txnid + "|" + order.razorpay_payment_id

            def create_sha256_signature(key, message):
                key = key.encode()
                message = message.encode()
                return hmac.new(key, message, hashlib.sha256).hexdigest()

            generated_signature = create_sha256_signature(r_key_secret, message_conc)
            if (generated_signature == order.razorpay_signature):
                order.payment_done = True
                order.save()

                for rs in ordered_products:
                    product = Product.objects.get(id=rs.product_id)
                    product.quantity_on_stock -= rs.quantity
                    product.save()

                plain_text = get_template('order/email/order_confirmed.txt')
                rendered_html = get_template('order/email/order_confirmed.html')
                context_data = {'order': order, 'ordered_products': ordered_products, }
                email_subject = "Your Order is Confirmed"
                from_email = DEFAULT_FROM_EMAIL
                to_email = request.user.email
                text_content = plain_text.render(context_data)
                html_content = rendered_html.render(context_data)
                email = EmailMultiAlternatives(email_subject, text_content, from_email, [to_email])
                email.attach_alternative(html_content, "text/html")
                email.send()

        else:
            order.status = 'Failed'
            order.save()
            return redirect("order_failed_now")
    else:
        if order.payment_done == False:
            order.status = 'Failed'
            order.save()
        return redirect("order_failed_now")

    messages.success(request, "Your Order has been Successfully Completed. Thank You.")
    return render(request, "order/order_completed.html", {"order": order, "ordered_products": ordered_products, })



@login_required(login_url='account_login')
def order_failed_now(request):
    messages.error(request, "Your Order is Failed. Please Try Again.")
    return render(request, "order/order_failed.html")
    
