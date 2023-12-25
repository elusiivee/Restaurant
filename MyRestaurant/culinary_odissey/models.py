from django.db import models

# Create your models here.

class DishCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)