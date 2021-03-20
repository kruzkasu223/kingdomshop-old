from django.urls import path
from order import views


urlpatterns = [
    path('', views.cart, name="cart"),
    path('add-to-cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('minus-to-cart/<int:id>', views.minus_to_cart, name='minus_to_cart'),
    path('delete-from-cart/<int:id>', views.delete_from_cart, name='delete_from_cart'),
    path('place-order/', views.place_order, name='place_order'),
    path('order-completed-cart/', views.order_completed_cart, name='order_completed_cart'),
    path('order-failed-cart/', views.order_failed_cart, name='order_failed_cart'),
    path('buy-now/<int:id>-<str:slug>-<str:sku>', views.buy_now, name='buy_now'),
    path('order-completed-now/', views.order_completed_now, name='order_completed_now'),
    path('order-failed-now/', views.order_failed_now, name='order_failed_now'),
    
]