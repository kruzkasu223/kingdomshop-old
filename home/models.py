from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.forms import ModelForm, TextInput, Textarea
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class About(models.Model):
    about_title = models.CharField(max_length=254, blank=True, null=True)
    about_us = RichTextUploadingField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.about_title


class CompanySocialMedia(models.Model):
    csm_name = models.CharField(max_length=254)
    csm_url = models.CharField(max_length=254)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Company Social Media")
        verbose_name_plural = _("Company Social Medias")
    
    def __str__(self):
        return self.csm_name


class ContactFormModel(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    subject = models.CharField(max_length=254)
    message = models.TextField()
    status = models.CharField(choices=STATUS,default='New', max_length=254)
    ip = models.CharField(max_length=254)
    note = models.CharField(max_length=512, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Contact Form")
        verbose_name_plural = _("Contact Forms")
    
    def __str__(self):
        return self.subject


class ContactForm(ModelForm):
    class Meta:
        model = ContactFormModel
        fields = ['name', 'email', 'subject','message']
        widgets = {
            'name': TextInput(attrs={'class': 'form-input', 'id':'form-name', 'required': 'true', }),
            'email': TextInput(attrs={'class': 'form-input', 'id':'form-email', 'required': 'true', }),
            'subject': TextInput(attrs={'class': 'form-input', 'id':'form-subject', 'required': 'true', }),
            'message': Textarea(attrs={'class': 'form-input form-msg', 'id':'form-msg', 'required': 'true', }),
        }


class Policy(models.Model):
    policy_name = models.CharField(max_length=254)
    policy_details = RichTextUploadingField()
    slug = models.SlugField(unique=True, primary_key=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Policy")
        verbose_name_plural = _("Policies")
    
    def __str__(self):
        return self.policy_name
        
    def get_absolute_url(self):
        return reverse('policy_detail', kwargs={'slug': self.slug})
    


class FAQ(models.Model):
    question = models.CharField(max_length=254)
    answer = RichTextUploadingField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")
    
    def __str__(self):
        return self.question
        


class SliderCarousel(models.Model):
    title = models.CharField(max_length=254)
    order = models.IntegerField()
    slider_image = models.ImageField(upload_to='images/slider/', null=True)
    url = models.URLField(max_length=254, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Slider Image")
        verbose_name_plural = _("Slider Images")
    
    def __str__(self):
        return self.title
    
    def sliderImage_tag(self):
        if self.slider_image.url is not None:
            return mark_safe('<img src="{}" height="50" width="100" style="object-fit:cover;"/>'.format(self.slider_image.url))
        else:
            return ""
            

