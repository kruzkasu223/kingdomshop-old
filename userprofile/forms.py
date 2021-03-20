from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, NumberInput, Select, HiddenInput
from userprofile.models import UserDetail, UserAddress
from allauth.account.forms import SignupForm
from product.models import Review


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=254, label='First Name', widget=forms.TextInput(attrs={'class': 'cont-input', 'id': 'contact-name', 'required': 'true', }))
    last_name = forms.CharField(max_length=254, label='Last Name', widget=forms.TextInput(attrs={'class': 'cont-input', 'id': 'contact-name', 'required': 'true', }))
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
    


class UpdateUserName(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', )
        widgets = {
            'first_name': TextInput(),
            'last_name': TextInput(),
        }
        


class UpdateUserDetails(UserChangeForm):
    class Meta:
        model = UserDetail
        fields = ('phone', 'age', 'gender', )
        widgets = {
            'phone': NumberInput(),
            'age': NumberInput(),
            'gender': Select(),
        }
        


class UpdateUserAddress(UserChangeForm):
    class Meta:
        model = UserAddress
        fields = ('address_line_1', 'address_line_2', 'pincode', 'city', 'state', )
        widgets = {
            'address_line_1': TextInput(),
            'address_line_2': TextInput(),
            'pincode': NumberInput(),
            'city': TextInput(),
            'state': Select(),
        }
        


class ReviewUpdate(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'review', 'rating', ]
    

