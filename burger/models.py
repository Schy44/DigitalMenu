from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class Member (models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    alt_text = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class BurgerMenu(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    alt_text = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class ChefSpecial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    alt_text = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Userprofile(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    favorite_burger = models.CharField(max_length=100)

    def __str__(self):
        return self.username
