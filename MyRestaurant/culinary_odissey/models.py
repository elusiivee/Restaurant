from django.db import models


# Create your models here.

class DishCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Disch categories'
        ordering = ('order',)

    def __str__(self):
        return f'{self.name}'

    def __iter__(self):
        dishes = self.dishes.filter(is_visible=True)
        for dish in dishes:
            yield dish


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')
    ingredients = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='dishes/', blank=True)
    category = models.ForeignKey(DishCategory, on_delete=models.PROTECT, related_name='dishes')
    is_visible = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'Dishes'
        ordering = ('order',)
        constraints = [
            models.UniqueConstraint(fields=['order', 'category'], name='unique_order_per_each_category'),
        ]
        unique_together = ['id', 'slug']

    def __str__(self):
        return f'{self.name}'
