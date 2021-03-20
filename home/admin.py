from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from home.models import *


admin.site.site_header = "Kingdom Shop"
admin.site.site_title = "Kingdom Shop"


class SliderCarouselAdmin(admin.ModelAdmin):
    list_display = ['order', 'sliderImage_tag', 'title', ]
    readonly_fields = ('sliderImage_tag', 'updated_at', 'created_at', )


class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('updated_at', 'created_at', )


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'status', 'updated_at',]
    readonly_fields =('user_link', 'name', 'subject', 'email', 'message', 'ip', 'updated_at', 'created_at', )
    exclude = ('user', )
    list_filter = ['status']
    search_fields = ('name', 'subject', )

    def user_link(self, obj):
        return mark_safe('<b><a href="{}">{}</a></b>'.format(
            reverse("admin:auth_user_change", args=(obj.user.pk,)),
            obj.user.first_name + " " + obj.user.last_name
        ))
        user_link.short_description = 'user'


class PolicyAdmin(admin.ModelAdmin):
    readonly_fields = ('updated_at', 'created_at', )
    prepopulated_fields = {'slug': ('policy_name',)}


class CompanySocialMediaAdmin(admin.ModelAdmin):
    readonly_fields = ('updated_at', 'created_at', )


class FAQAdmin(admin.ModelAdmin):
    readonly_fields = ('updated_at', 'created_at', )


admin.site.register(About, AboutAdmin)
admin.site.register(CompanySocialMedia, CompanySocialMediaAdmin)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(SliderCarousel, SliderCarouselAdmin)
admin.site.register(ContactFormModel ,ContactFormAdmin)