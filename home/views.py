from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from home.models import *
from product.models import *
from django.db.models import Q
from django.core.paginator import Paginator


def home(request):
    slider = SliderCarousel.objects.order_by('order')
    
    product_trending = Product.objects.all().order_by("-views")[:5]
    product_recent = Product.objects.all().order_by("-id")[:5]
    
    context = {"slider": slider, "product_trending": product_trending, "product_recent": product_recent, }
    return render(request, "home/home.html", context)
    


def about(request):
    about = About.objects.get(pk=1)
    
    context = {"about": about, }
    return render(request, "home/about.html", context)
    


def policy(request):
    policy = Policy.objects.all()
    context = {"policy": policy, }
    return render(request, "home/policy.html", context)
    


def policyView(request, slug):
    policy_view = Policy.objects.get(pk=slug)
    context = {"policy": policy_view, }
    return render(request, "home/policybase.html", context)
    


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormModel()
            if request.user.is_authenticated:
                current_user = request.user
                data.user_id = current_user.id
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            
            messages.success(request,"Your Message Has Been Sent Successfully! We Will Contact You As Soon As Possible.")
            return HttpResponseRedirect('/contact')
    
    form = ContactForm
    
    context = {"form": form, }
    return render(request, "home/contact.html", context, )
    


def faqs(request):
    faqs = FAQ.objects.all()
    context = {"faqs": faqs, }
    return render(request, "home/faqs.html", context)
    


def search(request):
    query = request.GET.get('query')
    if query:
        products = Product.objects.filter(Q(title__icontains=query) | Q(detailed_desc__icontains=query) | Q(keywords__icontains=query) | Q(description__icontains=query)).order_by('id')
        paginator = Paginator(products, 10)
        page = request.GET.get('page', 1)
        products = paginator.get_page(page)
    else:
        products = ''

    context = {"products": products, "query": query, }
    return render(request, "home/search.html", context)
    


def my_page_not_found_view(request, *args, **kwargs):
    error_name = "Error 404 - Page Not Found"
    context = {'error': error_name}
    return render(request, 'error.html', context, status=404)

def my_error_view(request, *args, **kwargs):
    error_name = "Error 500 - Server Error"
    context = {'error': error_name}
    return render(request, 'error.html', context, status=500)

def my_permission_denied_view(request, *args, **kwargs):
    error_name = "Error 403 - Permission Denied"
    context = {'error': error_name}
    return render(request, 'error.html', context, status=403)

def my_bad_request_view(request, *args, **kwargs):
    error_name = "Error 400 - Bad Request"
    context = {'error': error_name}
    return render(request, 'error.html', context, status=400)