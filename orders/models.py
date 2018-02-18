from django.db import models
from seller.models import Seller
from driver.models import Driver
from areas.models import Zone, Location
from financials.models import Financial

# Create your models here.

class Order(models.Model):
    date_received = models.DateTimeField()
    closed = models.DateTimeField(null=True, blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    amount_dollars = models.FloatField()
    amount_lebanese = models.FloatField()
    customer = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=100)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    financial_status = models.ForeignKey(Financial, on_delete=models.CASCADE)
    actual_amount = models.FloatField()

    def __str__(self):
        return str(self.id)


class OrderHistory(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    financial_status = models.ForeignKey(Financial, on_delete=models.CASCADE)
    update = models.TextField(null=True, blank=True)
