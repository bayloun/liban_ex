from django.db import models
from seller.models import Seller
from driver.models import Driver
from areas.models import Zone, Location

# Create your models here.

class Order(models.Model):
    date_received = models.DateTimeField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    amount = models.IntegerField()
    customer = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=100)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
