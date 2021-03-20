from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Avg, Count
from django.forms import ModelForm, TextInput, Textarea
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.utils.translation import gettext_lazy as _


class Category(MPTTModel):
    parent = TreeForeignKey('self', blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=254, null=False, unique=True)
    keywords = models.CharField(max_length=254)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to='images/category')
    slug = models.SlugField(null=False, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
    
    class MPTTMeta:
        order_insertion_by = ['title']
    
    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' > '.join(full_path[::-1])
    


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    varient_parent = models.ManyToManyField('self', blank=True)
    varient_size = models.CharField(max_length=254, blank=True, null=True)
    varient_colour = models.CharField(max_length=254, blank=True, null=True)
    views = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    sku = models.CharField(max_length=254, null=False, unique=True)
    title = models.CharField(max_length=70)
    keywords = models.CharField(max_length=254)
    description = models.TextField()
    brand = models.CharField(max_length=254, blank=True, null=True)
    image = models.ImageField(upload_to='images/product/', null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    discount_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    quantity_on_stock = models.IntegerField(default=100)
    detailed_desc = RichTextUploadingField()
    slug = models.SlugField(null=False, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})
    
    def average_rating(self):
        reviews = Review.objects.filter(product=self).aggregate(average=Avg("rating"))
        avg = 0
        if reviews["average"] is not None:
            avg = float(reviews["average"])
        return avg
    
    def count_review(self):
        reviews = Review.objects.filter(product=self).aggregate(count=Count("id"))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
    


class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=254, blank=True)
    image = models.ImageField(blank=True, upload_to='images/product/')

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")

    def __str__(self):
        return self.title
        
    def images_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
    


class Review(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Show', 'Show'),
        ('Spam', 'Spam'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="2")
    rating = models.IntegerField(default=5)
    title = models.CharField(max_length=254, null=True, blank=True)
    review = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STATUS, default='New', max_length=254)
    ip = models.CharField(max_length=254)
    note = models.CharField(max_length=512, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Review")
        verbose_name_plural = _("Product Reviews")
    
    def __str__(self):
        return self.product.title
    


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'title', 'review']
        widgets = {
            'title': TextInput(attrs={'class': 'cont-input', 'id':'contact-subject', 'required': 'true', }),
            'review': Textarea(attrs={'class': 'cont-input cont-msg', 'id':'contact-msg', 'required': 'true', }),
        }
    
