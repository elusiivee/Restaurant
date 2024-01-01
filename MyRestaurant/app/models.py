import os

from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField
from django.core.files.images import ImageFile

class MainMenueItems(models.Model):
    title = models.CharField(max_length=50, verbose_name='menu item')
    slug = models.SlugField(max_length=50, db_index=True, verbose_name='url')
    is_manager = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField()

    def get_absolute_url(self):
        return self.slug

    def __str__(self):
        return f'{self.title}/{self.slug}'

    class Meta:
        ordering = ('order',)


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='slider title')
    photo = models.ImageField(upload_to='main_slider/', blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class Chefs(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    twitter_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    photo = models.ImageField(upload_to='chefs/', blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Chefs'


class Customers(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    comment = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='customers/',)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Customers'


class Footer(models.Model):
    title = RichTextField()
    opening_hours = RichTextField()
    newsletter = RichTextField()
    twitter_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    copyright_text = RichTextField()

    def __str__(self):
        return 'Footer info'

