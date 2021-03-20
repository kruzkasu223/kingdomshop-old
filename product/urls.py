from django.urls import path, include
from product import views


urlpatterns = [
    path('all/', views.products, name="product_all"),
    path('categories/', views.categories, name="categories"),
    path('category/<int:id>-<slug:slug>', views.category_products, name="category_products"),
    path('<int:id>-<slug:slug>-<str:sku>/', views.product_view, name="product_view"),
    path('postreview/<int:id>/', views.post_review, name='post_review'),
    path('<int:id>-<slug:slug>-<str:sku>/reviews', views.product_reviews, name="product_reviews"),
    
]