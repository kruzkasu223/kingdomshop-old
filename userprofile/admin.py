from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import *


class UserDetailAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'age', 'gender']
    readonly_fields = ('user_link', 'phone', 'age', 'gender', )
    exclude = ('user', )

    def user_link(self, obj):
        return mark_safe('<b><a href="{}">{}</a></b>'.format(
            reverse("admin:auth_user_change", args=(obj.user.pk,)),
            obj.user.first_name + " " + obj.user.last_name
        ))
    user_link.short_description = 'user'
    


class WishlistAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', ]
    readonly_fields = ('user_link', 'product_link', 'created_at', )
    exclude = ('user', 'product' )

    def user_link(self, obj):
        return mark_safe('<b><a href="{}">{}</a></b>'.format(
            reverse("admin:auth_user_change", args=(obj.user.pk,)),
            obj.user.first_name + " " + obj.user.last_name
        ))
    user_link.short_description = 'user'

    def product_link(self, obj):
        return mark_safe('<b><a href="{}">{}</a></b>'.format(
            reverse("admin:product_product_change", args=(obj.product.pk,)),
            obj.product
        ))
    product_link.short_description = 'product'
    

class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'state', ]
    list_filter = ['state', ]
    readonly_fields = ('user_link', 'address_line_1', 'address_line_2', 'pincode', 'city', 'state', )
    exclude = ('user', )

    def user_link(self, obj):
        return mark_safe('<b><a href="{}">{}</a></b>'.format(
            reverse("admin:auth_user_change", args=(obj.user.pk,)),
            obj.user.first_name + " " + obj.user.last_name
        ))
    user_link.short_description = 'user'


admin.site.register(UserDetail, UserDetailAdmin)
admin.site.register(UserAddress, UserAddressAdmin)
admin.site.register(Wishlist, WishlistAdmin)