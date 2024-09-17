from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Info(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(default = "")
    phone_number = models.CharField(max_length=15,validators=[RegexValidator(r'^\d+$', 'Only numeric values are allowed')])
    address= models.TextField(default="")
