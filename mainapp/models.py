from django.db import models

# Create your models here.


class City(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'
