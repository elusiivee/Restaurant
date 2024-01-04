from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=60, )
    content = RichTextField()
    photo = models.ImageField(upload_to='blog/')
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-updated_at']