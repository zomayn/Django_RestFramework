from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    # borrowed = models.BooleanField(default=False)
    # borrowedOn = models.DateTimeField()

    def __str__(self):
        return self.name
