from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.utils.translation import gettext_lazy as _


GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True, unique=True)
    age = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    gender = models.CharField(max_length=254, choices=GENDER, blank=True, null=True)

    class Meta:
        verbose_name = _("User Detail")
        verbose_name_plural = _("User Details")
    
    def __str__(self):
        return self.user.username
    
    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name
    


STATES = (
    ("Andaman and Nicobar Islands (UT)","Andaman and Nicobar Islands (UT)"),
    ("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh ","Arunachal Pradesh "),
    ("Assam","Assam"),
    ("Bihar","Bihar"),
    ("Chandigarh (UT)","Chandigarh (UT)"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Dadra and Nagar Haveli and Daman and Diu (UT)","Dadra and Nagar Haveli and Daman and Diu (UT)"),
    ("Delhi (NCT)","Delhi (NCT)"),
    ("Goa","Goa"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jammu and Kashmir (UT)","Jammu and Kashmir (UT)"),
    ("Jharkhand","Jharkhand"),
    ("Karnataka","Karnataka"),
    ("Kerala","Kerala"),
    ("Ladakh (UT)","Ladakh (UT)"),
    ("Lakshadweep (UT)","Lakshadweep (UT)"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),
    ("Odisha","Odisha"),
    ("Puducherry (UT)","Puducherry (UT)"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("Tamil Nadu","Tamil Nadu"),
    ("Telangana","Telangana"),
    ("Tripura","Tripura"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal"),
)


class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=254, null=True)
    address_line_2 = models.CharField(max_length=254, blank=True, null=True)
    pincode = models.DecimalField(max_digits=6, decimal_places=0, null=True)
    city = models.CharField(max_length=254, null=True)
    state = models.CharField(max_length=254, choices=STATES, null=True)

    class Meta:
        verbose_name = _("User Address")
        verbose_name_plural = _("User Addresses")
    
    def __str__(self):
        return self.user.username
    


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Wishlist")
        verbose_name_plural = _("Wishlist")
    
    def __str__(self):
        return self.product.title
    

