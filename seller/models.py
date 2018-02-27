from django.db import models

# Create your models here.

class Seller(models.Model):
    business_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    operations_phone_number = models.CharField(max_length=20)
    lebanon_rate = models.FloatField(null=True, blank=True)
    beirut_rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.business_name
