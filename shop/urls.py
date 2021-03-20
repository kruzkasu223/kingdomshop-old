from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('product/categories/sarees/admin/', admin.site.urls),
    
    path('', include('home.urls'), name="home"),
    path('product/', include('product.urls'), name='product'),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', include('userprofile.urls')),
    path('product/cart/', include('order.urls')),
    
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'home.views.my_page_not_found_view'
handler500 = 'home.views.my_error_view'
handler403 = 'home.views.my_permission_denied_view'
handler400 = 'home.views.my_bad_request_view'
