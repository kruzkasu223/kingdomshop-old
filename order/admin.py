from django.contrib import admin
from order.models import *
from django.utils.safestring import mark_safe
from django.urls import reverse


class CartAdmin(admin.ModelAdmin):
    list_display = ['product','user','quantity', 'price', 'totalPrice' ]
    readonly_fields = ('user_link', 'product_link', 'quantity', 'price', 'totalPrice' )
    exclude = ('user', 'product', )

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
    


class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user_link', 'sku', 'product_link', 'price', 'quantity', 'totalPrice', )
    exclude = ('user', 'product' )
    extra = 0

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


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_txnid', 'payment_txnid', 'payment_done', 'razorpay_payment_id', 'razorpay_signature', 'user_link',  'total', 'first_name', 'last_name', 'email', 'phone', 'address_line_1', 'address_line_2', 'pincode', 'city', 'state', 'note', 'ip', 'created_at', 'updated_at', )
    exclude = ('user', )
    list_display = ['order_txnid', 'payment_done', 'razorpay_payment_id', 'status', 'user', 'total', 'state', ]
    list_filter = ['status', 'state', ]
    list_editable = ['status', ]
    inlines = [OrderProductline]

    def user_link(self, obj):
        return mark_safe('<b><a href="{}">{}</a></b>'.format(
            reverse("admin:auth_user_change", args=(obj.user.pk,)),
            obj.user.first_name + " " + obj.user.last_name
        ))
    user_link.short_description = 'user'
    


class OrderProductAdmin(admin.ModelAdmin):
    readonly_fields = ('order_link', 'user_link', 'sku', 'product_link', 'price', 'quantity', 'totalPrice', )
    exclude = ('order', 'user', 'product' )
    list_display = ['product', 'order', 'user', 'quantity', 'price', 'totalPrice' ]

    def order_link(self, obj):
        return mark_safe('<b><a href="{}">{}</a></b>'.format(
            reverse("admin:order_order_change", args=(obj.order.pk,)),
            obj.order.order_txnid
        ))
    order_link.short_description = 'order'
    
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




admin.site.register(Cart, CartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)