from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Shop(models.Model):
    SERVICE   = 'S'
    PRODUCT = 'P'
    BUSINESS_CHOICES = (
        (SERVICE, 'Service'),
        (PRODUCT, 'Product')
    )

    AUTOMOTIVE = 'Automotive'
    HEALTH_AND_BEAUTY = 'Health_and_Beauty'
    TECHNOLOGY = 'Technology'
    CREATIVE= 'Creative'
    SKILLED_TRADE = 'Skilled Trade'
    LESSONS_AND_TUTORING = 'Lessons_and_Tutoring'
    PET = 'Pet'
    LEGAL = 'Legal'
    LABOR = 'Labor'
    GENERAL = 'General'
    SERVICE_CHOICES = (
        (AUTOMOTIVE, 'Automotive'),
        (HEALTH_AND_BEAUTY, 'Health and Beauty'),
        (TECHNOLOGY, 'Technology'),
        (CREATIVE, 'Creative'),
        (SKILLED_TRADE, 'Skilled Trade'),
        (LESSONS_AND_TUTORING, 'Lessons and Tutoring'),
        (PET, 'Pet'),
        (LEGAL, 'Legal'),
        (LABOR, 'Labor'),
        (GENERAL, 'General')
    )

    ANTIQUES_AND_COLLECTABLES = 'Antiques and Collectibles'
    ARTS_AND_CRAFTS = 'Arts and Crafts'
    FOOD = 'Food'
    FASHION = 'Fashion'
    HEALTH_AND_BEAUTY = 'Health and Beauty'
    TECHNOLOGY = 'Technology'
    TOOLS_AND_EQUIPMENT = 'Tools and Equipment'
    HOME = 'Home'
    GENERAL = 'General'
    PRODUCT_CHOICES = (
        (ANTIQUES_AND_COLLECTABLES, 'Antiques and Collectibles'),
        (ARTS_AND_CRAFTS, 'Arts and Crafts'),
        (FOOD, 'Food'),
        (FASHION, 'Fashion'),
        (HEALTH_AND_BEAUTY, 'Health and Beauty'),
        (TECHNOLOGY, 'Technology'),
        (TOOLS_AND_EQUIPMENT, 'Tools and Equipment'),
        (HOME, 'Home'),
        (GENERAL, 'General')
    )
    # about business
    name = models.CharField(max_length=500)
    # From Choices
    business_type = models.CharField(max_length=10, choices=BUSINESS_CHOICES)
    product_type = models.CharField(max_length=30, choices=PRODUCT_CHOICES, default=GENERAL)
    service_type = models.CharField(max_length=30, choices=SERVICE_CHOICES, default=GENERAL)
    description = models.CharField(max_length=512)
    # About Student Owner
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_bio = models.CharField(max_length=512)
    def __str__(self):
        return self.name


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    text = models.CharField(max_length=512)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Tokens():
    def create_user_tokens():
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)


#Eventually we can add help wanted section
