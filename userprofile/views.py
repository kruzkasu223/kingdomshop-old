from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from userprofile.models import UserDetail, UserAddress, Wishlist
from home.models import Policy, CompanySocialMedia
from product.models import Product, Review
from userprofile.forms import UpdateUserName, UpdateUserDetails, UpdateUserAddress, ReviewUpdate
from order.models import Order, OrderProduct
from django.core.paginator import Paginator


@login_required(login_url='account_login')
def userprofile(request):
    current_user = request.user
    userdetail = UserDetail.objects.get(user_id=current_user.id)
    useraddress = UserAddress.objects.get(user_id=current_user.id)
    
    context = {"userdetail": userdetail, "useraddress": useraddress, "user": current_user, }
    return render(request, "userprofile/userprofile.html", context)
    


@login_required(login_url='account_login')
def update_user_name(request):
    if request.method == 'POST':
        form = UpdateUserName(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Name has been updated!')
            return redirect(userprofile)
    else:
        form = UpdateUserName(instance=request.user)
        context = {"form": form, }
        return render(request, "userprofile/update_user_name.html", context)
    


@login_required(login_url='account_login')
def update_user_details(request):
    if request.method == 'POST':
        form = UpdateUserDetails(request.POST, instance=request.user.userdetail)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Details has been updated!')
            return redirect(userprofile)
    else:
        form = UpdateUserDetails(instance=request.user.userdetail)
        context = {"form": form, }
        return render(request, "userprofile/update_user_details.html", context)
    


@login_required(login_url='account_login')
def update_user_address(request):
    if request.method == 'POST':
        form = UpdateUserAddress(request.POST, instance=request.user.useraddress)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Address has been updated!')
            return redirect(userprofile)
    else:
        form = UpdateUserAddress(instance=request.user.useraddress)
        context = {"form": form, }
        return render(request, "userprofile/update_user_address.html", context)
    


@login_required(login_url='account_login')
def user_reviews(request):
    current_user = request.user
    reviews = Review.objects.filter(user_id=current_user.id).order_by("-id")
    paginator = Paginator(reviews, 10)
    page = request.GET.get('page', 1)
    reviews = paginator.get_page(page)
    
    context = {"reviews": reviews, }
    return render(request, "userprofile/user_reviews.html", context)
    


@login_required(login_url='account_login')
def user_reviews_update(request, id):
    current_user = request.user
    review = Review.objects.get(id=id, user_id=current_user.id)
    
    if request.method == 'POST':
        form = ReviewUpdate(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Review has been updated!')
            return redirect('user_reviews')
    
    form = ReviewUpdate(instance=review)
    context = {"review": review, "form": form, }
    return render(request, "userprofile/user_review_update.html", context)
    


@login_required(login_url='account_login')
def user_reviews_delete(request, id):
    current_user = request.user
    Review.objects.filter(id=id, user_id=current_user.id).delete()
    
    messages.error(request, 'Your Review has been deleted.')
    return redirect('user_reviews')
    
    


@login_required(login_url='account_login')
def wishlist(request):
    current_user = request.user
    wishlist = Wishlist.objects.filter(user_id=current_user.id).order_by("-id")
    paginator = Paginator(wishlist, 10)
    page = request.GET.get('page', 1)
    wishlist = paginator.get_page(page)
    
    context = {"wishlist": wishlist, }
    return render(request, "userprofile/wishlist.html", context)
    


@login_required(login_url='account_login')
def wishlist_add(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    product= Product.objects.get(id=id)
    checkinproduct = Wishlist.objects.filter(product_id=id, user_id=current_user.id)
    
    if checkinproduct:
        control = 1
    else:
        control = 0
    
    if control == 1:
        pass
    else:
        data = Wishlist()
        data.user_id = current_user.id
        data.product_id = id
        data.save()
        messages.success(request, "Product added to your Wishlist")
        return HttpResponseRedirect(url)
    


@login_required(login_url='account_login')
def wishlist_delete(request, id):
    Wishlist.objects.filter(id=id).delete()
    messages.error(request, 'Product has beem deleted from your Wishlist.')
    return redirect('wishlist')
    


@login_required(login_url='account_login')
def user_orders(request):
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id)
    ordered_products = OrderProduct.objects.filter(user_id=current_user.id)

    for order in orders:
        if order.payment_done is False and order.status != "Failed":
            order.status = "Failed"
            order.save()
    
    your_orders = Order.objects.filter(user_id=current_user.id).order_by("-id")
    paginator = Paginator(your_orders, 5)
    page = request.GET.get('page', 1)
    your_orders = paginator.get_page(page)

    context = {"orders": your_orders, "ordered_products": ordered_products, }
    return render(request, 'userprofile/user_orders.html', context)
    

