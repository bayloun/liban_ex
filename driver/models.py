from django.db import models

# Create your models here.

class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=40)

    old_id = models.CharField(max_length=100)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name + " " + self.last_name
