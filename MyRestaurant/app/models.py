import os

from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField
from django.core.files.images import ImageFile


class MainMenueItems(models.Model):
    '''
    Model representing menu items.

    Fields:
        title (CharField): Title of the menu item.
        slug (SlugField): URL slug for the menu item
        is_manager (BooleanField): Indicates if the menu item is managed (True/False).
        is_visible (BooleanField): Indicates if the menu item should be visible on the website.
        order (PositiveSmallIntegerField): Order in which the menu item should appear.

    '''
    title = models.CharField(max_length=50, verbose_name='menu item')
    slug = models.SlugField(max_length=50, db_index=True, verbose_name='url')
    is_manager = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField()

    def get_absolute_url(self):
        '''
        Returns the URL for the menu item.
        '''
        return self.slug

    def __str__(self) -> str:
        '''
        String representation of the menu item, used in admin.
        '''
        return f'{self.title}/{self.slug}'

    class Meta:
        '''
        Meta class specifying the default ordering for the model.
        '''
        ordering = ('order',)


class Slider(models.Model):
    '''
    Model representing slider items.

    Fields:
        title (CharField): Title of the sliders item.
        photo (ImageField): Background of the sliders. Uploading to in .main_slider/.
        is_visible (BooleanField): Indicates if the slider item should be visible on the website.
    '''
    title = models.CharField(max_length=200, verbose_name='slider title')
    photo = models.ImageField(upload_to='main_slider/', blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.title}'


class About(models.Model):
    '''
    Model representing about items.

    Fields:
        title (CharField): Title of the about item.
        description (TextField) : Main text of the section.
    '''
    title = models.CharField(max_length=50, verbose_name='menu item')
    description = models.TextField()

    def __str__(self) -> str:
        return 'About section'


class Progress(models.Model):
    '''
    Model representing progress items.

    Fields:
        title (CharField): Title of the section 'progress' item.
        description (TextField) : Main text of the section.
        value (FloatField) : Value of the progress.
        is_visible (BooleanField): Indicates if the progress item should be visible on the website.
    '''
    title = models.CharField(max_length=100, verbose_name='progress title')
    value = models.FloatField()
    is_visible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.title}'


class Services(models.Model):
    '''
    Model representing services items.

    Fields:
        title (CharField): Title of the section 'services' item.
        description (TextField) : Main text of the section.
        photo (ImageField): Icons of the services. Uploading to in .services/.
        is_visible (BooleanField): Indicates if the services item should be visible on the website.
    '''
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='services/', )
    is_visible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Services'


class Chefs(models.Model):
    '''
    Model representing chefs in the culinary team.

    Fields:
        name (CharField): Chef's name.
        status (CharField): Professional status or title of the chef.
        description (CharField): Description of the chef.
        twitter_link (URLField): Link to the chef's Twitter profile (optional).
        facebook_link (URLField): Link to the chef's Facebook profile (optional).
        instagram_link (URLField): Link to the chef's Instagram profile (optional).
        photo (ImageField): Photo of the chef, uploaded to 'chefs/' directory.
        is_visible (BooleanField): Indicates whether the chef's profile should be visible on the website.
    '''
    name = models.CharField(max_length=100, verbose_name='name')
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    twitter_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    photo = models.ImageField(upload_to='chefs/', blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Chefs'


class Customers(models.Model):
    '''
    Model representing customers.

    Fields:
        name (CharField): Customer's name.
        comment (CharField): Customer's commnet.
        photo (ImageField): Photo of the customer, uploaded to 'customers/' directory.
        is_visible (BooleanField): Indicates whether the customer should be visible on the website.
    '''
    name = models.CharField(max_length=100, verbose_name='name')
    comment = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='customers/', )
    is_visible = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Customers'


class Footer(models.Model):
    '''
    Model representing footer information for the website.

    Fields:
        title (RichTextField): Title or heading for the footer.
        opening_hours (RichTextField): Text containing the opening hours information.
        newsletter (RichTextField): Text related to the newsletter.
        twitter_link (URLField): Link to the Twitter profile (optional).
        facebook_link (URLField): Link to the Facebook page (optional).
        instagram_link (URLField): Link to the Instagram profile (optional).
        copyright_text (RichTextField): Text displaying copyright information.
    '''
    title = RichTextField()
    opening_hours = RichTextField()
    newsletter = RichTextField()
    twitter_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    copyright_text = RichTextField()

    def __str__(self) -> str:
        return 'Footer info'
