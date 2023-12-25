from django.db import models

# Create your models here.

class DishCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural='Disch categories'
        ordering = ('order', )
    def __str__(self):
        return f'{self.name}'
