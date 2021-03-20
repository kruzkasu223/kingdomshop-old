from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from product.models import *
from home.models import Policy, CompanySocialMedia
from order.models import Cart, OrderProduct
from userprofile.models import Wishlist
from django.core.paginator import Paginator
from .filters import ProductFilter


def products(request):
    products = Product.objects.all().order_by("id")
    categories = Category.objects.all()
    products_filter = ProductFilter(request.GET, queryset=products)

    paginator = Paginator(products_filter.qs, 10)
    page = request.GET.get('page', 1)
    products = paginator.get_page(page)
    
    context = {"products": products, "categories": categories, }
    return render(request, "product/products.html", context)
    


def categories(request):
    categories = Category.objects.all()
    context = {"categories": categories, }
    return render(request, "product/categories.html", context)
    


def category_products(request, id, slug):
    category = Category.objects.get(id=id)
    category_product = Product.objects.filter(category_id=id).order_by("id")
    paginator = Paginator(category_product, 10)
    page = request.GET.get('page', 1)
    category_product = paginator.get_page(page)
    
    context = {"category_product": category_product, "category": category, }
    return render(request, "product/category_products.html", context)
    


def product_view(request, id, slug, sku):
    product = Product.objects.get(id=id)
    product_images = Images.objects.filter(product_id=id)
    product_reviews = Review.objects.filter(product_id=id).order_by("-rating")[:3]

    product.views += 1
    product.save()

    ordered_products = OrderProduct.objects.filter(user_id=request.user.id)
    user_post_review = False
    user_post_review_reached = False
    if ordered_products:
        for prod in ordered_products:
            if prod.product.id == product.id:
                user_post_review = True
                if prod.order.status == "Delivered" or prod.order.status == "Returned" or prod.order.status == "Refunded" or prod.order.status == "Returned & Refunded":
                    user_post_review_reached = True
    else:
        user_post_review = False

    category_product = Product.objects.filter(category_id=product.category_id).order_by("-views")[:5]

    try:
        if Cart.objects.get(product_id=id, user_id=request.user.id):
            cartItem = Cart.objects.get(product_id=id, user_id=request.user.id)
            if cartItem.quantity > 0:
                cart_empty = False
            else:
                cart_empty = True
        else:
            cart_empty = True
    except Exception as e:
        cart_empty = True
    
    try:
        if Review.objects.get(product_id=id, user_id=request.user.id):
            review = True
        else:
            review = False
    except Exception as e:
        review = False
    
    try:
        if Wishlist.objects.filter(product_id=id, user_id=request.user.id):
            wishlist_empty = False
        else:
            wishlist_empty = True
    except Exception as e:
        wishlist_empty = True
    
    context = {"product": product, "product_images": product_images, "product_reviews": product_reviews, "review": review, "cart_empty": cart_empty, "wishlist_empty": wishlist_empty, "category_product": category_product, "user_post_review": user_post_review, "user_post_review_reached": user_post_review_reached }
    return render(request, "product/product_view.html", context)
    


def post_review(request, id):
    url = request.META.get('HTTP_REFERER')
    
    if request.method == "POST":
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            data = Review()
            data.rating = form.cleaned_data['rating']
            data.title = form.cleaned_data['title']
            data.review = form.cleaned_data['review']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            
            messages.success(request, "Your Review has been posted and will showed up within 24 hours*. Thank You for posting Review.")
            return HttpResponseRedirect(url)
        else:
            messages.success(request, "Something is Wrong, Refresh your page and Please Fill all details correctly.")
            return HttpResponseRedirect(url)
        return HttpResponseRedirect(url)
    


def product_reviews(request, id, slug, sku):
    product = Product.objects.get(id=id)
    product_reviews = Review.objects.filter(product_id=id).order_by("-rating")
    paginator = Paginator(product_reviews, 10)
    page = request.GET.get('page', 1)
    product_reviews = paginator.get_page(page)

    try:
        if Review.objects.get(product_id=id, user_id=request.user.id):
            review = True
        else:
            review = False
    except Exception as e:
        review = False

    context = {"product": product, "product_reviews": product_reviews, "review": review, }
    return render(request, "product/product_reviews.html", context)