from django.db import models
import uuid
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from product.models import Product
from userprofile.models import STATES, UserDetail
from django.utils.translation import gettext_lazy as _
from shop.settings.current import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="2", null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Cart")
    
    def __str__(self):
        return self.product.title
    
    @property
    def price(self):
        if self.product.discount_price:
            return (self.product.discount_price)
        else:
            return (self.product.price)
    
    @property
    def totalPrice(self):
        if self.product.discount_price:
            return (self.quantity * self.product.discount_price)
        else:
            return (self.quantity * self.product.price)
        
    


class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']
    


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preaparing', 'Preaparing'),
        ('Despatched', 'Despatched'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
        ('Returned', 'Returned'),
        ('Refunded', 'Refunded'),
        ('Returned & Refunded', 'Returned & Refunded'),
        ('Failed', 'Failed'),
    )
    status = models.CharField(max_length=20, choices=STATUS,default='New')
    order_txnid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    payment_txnid = models.CharField(max_length=254, blank=True, null=True)
    payment_done = models.BooleanField(default=False)
    razorpay_payment_id = models.CharField(max_length=254, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=254, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="2", null=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    phone = models.DecimalField(max_digits=10, decimal_places=0)
    address_line_1 = models.CharField(max_length=254)
    address_line_2 = models.CharField(max_length=254, blank=True, null=True)
    pincode = models.DecimalField(max_digits=6, decimal_places=0)
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=254, choices=STATES)
    note = models.CharField(max_length=500, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    ip = models.CharField(blank=True, max_length=254)
    invoice = models.FileField(upload_to='invoices/%Y/%m/', null=True, blank=True)
    admin_note = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return str(self.order_txnid)

    def save(self):
        if self.id:
            old_order = Order.objects.get(pk=self.id)
            ordered_products = OrderProduct.objects.filter(order_id=self.id)
            inv = self.invoice

            if old_order.status != 'Despatched' and self.status == 'Despatched':
                plain_text = get_template('order/email/order_despatched.txt')
                rendered_html = get_template('order/email/order_despatched.html')
                context_data = {'order': self, 'ordered_products': ordered_products, }
                email_subject = "Your Order is Despatched"
                from_email = DEFAULT_FROM_EMAIL
                to_email = self.user.email
                text_content = plain_text.render(context_data)
                html_content = rendered_html.render(context_data)
                email = EmailMultiAlternatives(email_subject, text_content, from_email, [to_email])
                email.attach_alternative(html_content, "text/html")
                email.attach(inv.name, inv.read(), 'application/pdf')
                email.send()
                
            if old_order.status != 'Cancelled' and self.status == 'Cancelled':
                plain_text = get_template('order/email/order_cancelled.txt')
                rendered_html = get_template('order/email/order_cancelled.html')
                context_data = {'order': self, 'ordered_products': ordered_products, }
                email_subject = "Your Order is Cancelled"
                from_email = DEFAULT_FROM_EMAIL
                to_email = self.user.email
                text_content = plain_text.render(context_data)
                html_content = rendered_html.render(context_data)
                email = EmailMultiAlternatives(email_subject, text_content, from_email, [to_email])
                email.attach_alternative(html_content, "text/html")
                email.send()
                
            if old_order.status != 'Delivered' and self.status == 'Delivered':
                plain_text = get_template('order/email/order_delivered.txt')
                rendered_html = get_template('order/email/order_delivered.html')
                context_data = {'order': self, 'ordered_products': ordered_products, }
                email_subject = "Your Order is Delivered"
                from_email = DEFAULT_FROM_EMAIL
                to_email = self.user.email
                text_content = plain_text.render(context_data)
                html_content = rendered_html.render(context_data)
                email = EmailMultiAlternatives(email_subject, text_content, from_email, [to_email])
                email.attach_alternative(html_content, "text/html")
                email.send()
                
            if old_order.status != 'Refunded' and self.status == 'Refunded':
                plain_text = get_template('order/email/order_refunded.txt')
                rendered_html = get_template('order/email/order_refunded.html')
                context_data = {'order': self, 'ordered_products': ordered_products, }
                email_subject = "Your Order is Refunded"
                from_email = DEFAULT_FROM_EMAIL
                to_email = self.user.email
                text_content = plain_text.render(context_data)
                html_content = rendered_html.render(context_data)
                email = EmailMultiAlternatives(email_subject, text_content, from_email, [to_email])
                email.attach_alternative(html_content, "text/html")
                email.send()
                
        super(Order, self).save()



class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address_line_1', 'address_line_2', 'pincode', 'city', 'state', 'note', ]
        widgets = {
            'note': Textarea(),
        }
    


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="2", null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Ordered Product")
        verbose_name_plural = _("Ordered Products")

    def __str__(self):
        return self.product.title
    
    def sku(self):
        return self.product.sku
    
    @property
    def totalPrice(self):
        if self.product.discount_price:
            return (self.quantity * self.product.discount_price)
        else:
            return (self.quantity * self.product.price)
    


class QuantityForm(ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['quantity', ]
    

