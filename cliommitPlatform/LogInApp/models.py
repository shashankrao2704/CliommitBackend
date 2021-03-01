from django.db import models
from django.utils import timezone


# Create your models here.

class LogIn(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class RegistrationData(models.Model):
    # section 1
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    # section 2
    company = models.CharField(max_length=100, default='Null')
    country = models.CharField(max_length=100, default='Null')
    address = models.CharField(max_length=100, default='Null')
    reg_no = models.CharField(max_length=100, default='Null')
    employees = models.CharField(max_length=100, default='Null')
    sector = models.CharField(max_length=100, default='Null')
    turnover = models.CharField(max_length=100, default='Null')
    # section 3
    electricity = models.CharField(max_length=100, default='Null')
    air_travel = models.CharField(max_length=100, default='Null')
    automobile = models.CharField(max_length=100, default='Null')
    public_transport = models.CharField(max_length=100, default='Null')
    travel_accommodation = models.CharField(max_length=100, default='Null')
    waste = models.CharField(max_length=100, default='Null')
    water = models.CharField(max_length=100, default='Null')

    def __str__(self):
        return self.company
