from django.db import models
from pytz import unicode


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    imgpath = models.CharField(max_length=200)

    def __str__(self):
        return unicode(self.name)


class Branch(models.Model):
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return unicode(self.address)


class Contact(models.Model):
    VALUES = (
        (1, 'Phone'),
        (2, 'Facebook'),
        (3, 'Email'),
    )
    name = models.IntegerField(default=1, choices=VALUES)
    value = models.CharField(max_length=200)

    def __str__(self):
        return unicode(self.value)


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    logo = models.CharField(max_length=50)
    contacts = models.ForeignKey(Contact, related_name='contact', on_delete=models.CASCADE)
    branches = models.ForeignKey(Branch, related_name='branch', on_delete=models.CASCADE)
