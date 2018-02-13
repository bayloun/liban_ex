from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.location + " " + self.description

class Zone(models.Model):
    zone = models.CharField(max_length=100)

    def __str__(self):
        return self.zone
