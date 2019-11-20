from django.db import models

# Create your models here.
class PatientContact(models.Model):
    user_name = models.CharField(max_length=30, default="xxx")
    first_name = models.CharField(max_length=20, default='Jane')
    middle_name = models.CharField(max_length=20, default='Chandler')
    last_name = models.CharField(max_length=20, default='Doe')
    address = models.CharField(max_length=30, default='2662 Cannon Point Ct')
    city = models.CharField(max_length=20, default='Columbus')
    state = models.CharField(max_length=2, default='OH')
    zipCode = models.CharField(max_length=12, default='43209')
    homePhone = models.CharField(max_length=10, default='6144555678')
    cellPhone = models.CharField(max_length=10, default='6144567890')
    email = models.CharField(max_length=30, default='xu.285@franklin.edu')