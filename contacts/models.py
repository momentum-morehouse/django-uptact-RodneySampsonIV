from django.db import models
from django.core.validators import RegexValidator
from localflavor.us.models import USStateField, USZipCodeField
from django import forms
from django.db.models import Model



class Contact(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?\d{10}$',
        message="Phone number must be entered in the format: '+999-999-9999'.")

    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11,
                                    validators=[phone_regex],
                                    null=True,
                                    blank=True)
    address_1 = models.CharField(max_length=255, null=True, blank=True)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    zip_code = USZipCodeField(null=True, blank=True)
    birthday = models.DateField(null=True,blank=True)

class Note(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,related_name='notes')
    text = models.CharField(max_length=255, null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}, {self.nickname}'


# durm = City.objects.create(name="Durham", state="North Carolina",nickname="Bull City")