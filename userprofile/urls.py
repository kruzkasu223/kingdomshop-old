from django.urls import path, include
from userprofile import views


urlpatterns = [
    path('', views.userprofile, name="userprofile_home"),
    path('update_name/', views.update_user_name, name="update_user_name"),
    path('update_details/', views.update_user_details, name="update_user_details"),
    path('update_address/', views.update_user_address, name="update_user_address"),
    path('reviews/', views.user_reviews, name="user_reviews"),
    path('reviews/edit/<int:id>', views.user_reviews_update, name="user_reviews_update"),
    path('reviews/delete/<int:id>', views.user_reviews_delete, name="user_reviews_delete"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('wishlist/add/<int:id>', views.wishlist_add, name="wishlist_add"),
    path('wishlist/delete/<int:id>', views.wishlist_delete, name="wishlist_delete"),
    path('orders/', views.user_orders, name="user_orders"),
    
]