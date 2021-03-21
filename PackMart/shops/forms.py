from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Shop, Product, Review
from django.core.validators import EmailValidator
from django.utils.deconstruct import deconstructible

class ShopForm(forms.Form):
    BUSINESS_CHOICES = [
        ('SERVICE', 'Service'),
        ('PRODUCT', 'Product')
    ]
    PRODUCT_CHOICES = [
        ('ANTIQUES_AND_COLLECTABLES', 'Antiques and Collectibles'),
        ('ARTS_AND_CRAFTS', 'Arts and Crafts'),
        ('FOOD', 'Food'),
        ('FASHION', 'Fashion'),
        ('HEALTH_AND_BEAUTY', 'Health and Beauty'),
        ('TECHNOLOGY', 'Technology'),
        ('TOOLS_AND_EQUIPMENT', 'Tools and Equipment'),
        ('HOME', 'Home'),
        ('GENERAL', 'General')
    ]
    SERVICE_CHOICES = [
        ('AUTOMOTIVE', 'Automotive'),
        ('HEALTH_AND_BEAUTY', 'Health and Beauty'),
        ('TECHNOLOGY', 'Technology'),
        ('CREATIVE', 'Creative'),
        ('SKILLED_TRADE', 'Skilled Trade'),
        ('LESSONS_AND_TUTORING', 'Lessons and Tutoring'),
        ('PET', 'Pet'),
        ('LEGAL', 'Legal'),
        ('LABOR', 'Labor'),
        ('GENERAL', 'General')
    ]
    name = forms.CharField(label='Name', max_length=500)
    business_type = forms.ChoiceField(choices=BUSINESS_CHOICES, widget=forms.RadioSelect)
    product_type = forms.ChoiceField(choices=PRODUCT_CHOICES, widget=forms.RadioSelect, required=False)
    service_type = forms.ChoiceField(choices=SERVICE_CHOICES, widget=forms.RadioSelect, required=False)
    description = forms.CharField(label='Shop Description', max_length=512)
    owner_bio = forms.CharField(label='Tell us about yourself', max_length=512)
    logo = forms.ImageField(label='Logo (square)', required=False)
    banner_image = forms.ImageField(label='Banner Image', required=False)

class ProductForm(forms.Form):
    name = forms.CharField(label='Name', max_length=500)
    price = forms.IntegerField(label='Price')
    image = forms.ImageField(label='Banner Image', required=False)
    def __str__(self):
        return self.name


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Student Email')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if '@ncsu.edu' not in user.email:
            raise forms.ValidationError('Must an NCSU affiliated email address')
        if commit:
            user.save()
            return user
