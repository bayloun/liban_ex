from django.db import models
from orders.models import Order

# Create your models here.

class Financial(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status_choices = (
        ("Delivered", 'Delivered'),
        ("Refunded", 'Refunded'),
    )
    status = models.CharField(max_length=20, choices=status_choices)
    description = models.TextField()

    def __str__(self):
        return self.status
