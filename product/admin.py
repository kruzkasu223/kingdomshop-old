from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.admin import DraggableMPTTAdmin
from product import models
from product.models import *


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 4
    readonly_fields = ('images_tag',)

class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title', 'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at', )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)
                
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_count',
            cumulative=False)
            
        return qs
    
    def related_products_count(self, instance):
        return instance.products_count
    
    related_products_count.short_description = 'Related products (for this specific category)'
    
    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    
    related_products_cumulative_count.short_description = 'Related products (in tree)'
    


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'sku', 'category', 'image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag', 'created_at', 'updated_at', )
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['images_tag', 'product', 'title']
    readonly_fields = ('images_tag', 'product_link', 'product', )
    def product_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:product_product_change", args=(obj.product.pk,)),
            obj.product
        ))
    product_link.short_description = 'product'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'rating', 'title', 'status', 'user']
    list_filter = ['status', ]
    readonly_fields = ('product_link', 'user_link', 'rating', 'title', 'review', 'ip', 'created_at', 'updated_at', )
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
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Review, ReviewAdmin)