from django.db import models

# Create your models here.
class PatientLogin(models.Model):
    user_name = models.CharField(max_length=30, default='Jane')
    email = models.CharField(max_length=30, default='xxx@gmail.com')
    password = models.CharField(max_length=30, default='xxxx')