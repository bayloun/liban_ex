from django.db import models

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ['location']

    def __str__(self):
        return self.location

class Zone(models.Model):
    zone = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)

    class Meta:
        ordering = ['zone']

    def __str__(self):
        return self.zone + " " + self.description
