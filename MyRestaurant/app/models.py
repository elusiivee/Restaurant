from django.db import models
from ckeditor.fields import RichTextField
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


class Footer (models.Model):
    title = RichTextField()
    opening_hours=RichTextField()
    newsletter=RichTextField()
    twitter_link=models.URLField(blank=True)
    facebook_link=models.URLField(blank=True)
    instagram_link=models.URLField(blank=True)
    copyright_text=RichTextField()

    def __str__(self):
        return 'Footer info'