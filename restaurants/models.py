from django.db import models

# Create your models here.
from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=300)
    tools = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='images/', null=True)

    def __unicode__(self):
        return self.name
