from django.db import models

# Create your models here.
class Customer(models.Model):
    food_type = models.CharField(max_length=100)
    location = models.CharField(max_length=500)
    quanity = models.IntegerField()
    lifetime = models.DateField()
    bookingstatus = models.BooleanField()
