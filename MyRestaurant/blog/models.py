from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class Blog(models.Model):
    '''
    Model representing blog.

    Fields:
        title (CharField): Title of the section 'services' item.
        content (RichTextField): Content of the blog.
        photo (ImageField): Photo of the chef, uploaded to 'blog/' directory.
        updated_at (BooleanField): Indicates when blog is created (True/False).
        is_visible (BooleanField): Indicates whether the blog should be visible on the website.
    '''
    title = models.CharField(max_length=60, )
    content = RichTextField()
    photo = models.ImageField(upload_to='blog/')
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        ordering = ['-updated_at']
