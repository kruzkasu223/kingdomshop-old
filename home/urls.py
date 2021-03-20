from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.home, name="home" ),
    
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('policy/', views.policy, name="policy"),
    path('policy/<slug:slug>/', views.policyView, name="policy_view"),
    path('faqs/', views.faqs, name="faqs"),
    
    path('search/', views.search, name="search"),
    
]