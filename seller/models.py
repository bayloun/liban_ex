from django.db import models

# Create your models here.

class Seller(models.Model):
    business_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    operations_phone_number = models.CharField(max_length=20)

    def __str__(self):
        return "Business name: " + self.business_name + " Contact name: " + self.contact_name
