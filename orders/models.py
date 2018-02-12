from django.db import models

# Create your models here.

class Order(models.Model):
    delivered = models.BooleanField(default=False)
    random_field = models.CharField(max_length=400)
