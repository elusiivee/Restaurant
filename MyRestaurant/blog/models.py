from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class Blog(models.Model):
    '''
    Model representing chefs in the culinary team.

    Fields:
        title (CharField): Title of the section 'services' item.
        content (RichTextField): Content of the blog.
        photo (ImageField): Photo of the chef, uploaded to 'blog/' directory.
        (BooleanField): Indicates when blog is created (True/False).
        is_visible (BooleanField): Indicates whether the chef's profile should be visible on the website.
    '''
    title = models.CharField(max_length=60, )
    content = RichTextField()
    photo = models.ImageField(upload_to='blog/')
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-updated_at']