from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class DishCategory(models.Model):
    '''
    Model representing categories of dishes in the menu.

    Fields:
        name (CharField): Name of the dish category.
        order (PositiveSmallIntegerField): Order of the category within the menu.
        is_visible (BooleanField): Indicates whether the dish category is visible.

    Meta:
        verbose_name_plural (str): Plural name for the model in the admin interface.
        ordering (tuple): Specifies the default ordering of instances in queries.

    Methods:
        __str__(): Returns a string representation of the model instance.
        __iter__(): Iterator method to yield visible dishes within the category.
    '''
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
    '''
    Model representing dishes available in the menu.

    Fields:
        name (CharField): Name of the dish.
        slug (SlugField): URL-friendly version of the dish name for use in the website's URL.
        ingredients (CharField): List of ingredients used in the dish.
        price (DecimalField): Price of the dish.
        photo (ImageField): Photograph of the dish, uploaded to 'dishes/' directory.
        category (ForeignKey): Reference to the DishCategory to which the dish belongs.
        is_visible (BooleanField): Indicates whether the dish is visible on the menu.
        order (PositiveSmallIntegerField): Order of the dish within its category.

    Meta:
        verbose_name_plural (str): Plural name for the model in the admin interface.
        ordering (tuple): Specifies the default ordering of instances in queries.
        constraints (list): List of constraints on the model.
        unique_together (list): Ensures uniqueness of the combination of 'id' and 'slug'.

    Methods:
        __str__(): Returns a string representation of the model instance.
    '''
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


class Reservation(models.Model):
    '''
    Model representing customer reservations.

    Fields:
        name (CharField): Name of the person making the reservation.
        email (EmailField): Email address of the person making the reservation.
        phone (CharField): Phone number of the person making the reservation (validated with regex).
        date (DateField): Date of the reservation.
        time (TimeField): Time of the reservation.
        people (PositiveSmallIntegerField): Number of people in the reservation.
        is_processed (BooleanField): Indicates whether the reservation has been processed.
        created_at (DateTimeField): Date and time when the reservation was created (auto-generated).
        updated_at (DateTimeField): Date and time when the reservation was last updated (auto-generated).

    Methods:
        __str__(): Returns a string representation of the model instance.

    Meta:
        ordering (tuple): Specifies the default ordering of instances in queries.
    '''
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(validators=[phone_regex], max_length=20)
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveSmallIntegerField()
    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.people}'

    class Meta:
        ordering = ('-created_at',)
