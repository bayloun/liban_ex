from django.db import models

# Create your models here.

class Financial(models.Model):
    status_choices = (
        ("Undelivered", 'Undelivered'),
        ("Delivered with driver", 'Delivered with driver'),
        ("Delivered with company", 'Delivered with company'),
        ("Paid to seller", 'Paid to seller'),
    )
    status = models.CharField(max_length=20, choices=status_choices)
    description = models.TextField()

    def __str__(self):
        return self.status
