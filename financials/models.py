from django.db import models

# Create your models here.

class Financial(models.Model):
    status = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.status
