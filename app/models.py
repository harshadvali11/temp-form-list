from django.db import models

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=120)
    number=models.IntegerField()

    def __str__(self):
        return self.name