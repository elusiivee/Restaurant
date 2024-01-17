from django.contrib import admin
from .models import DishCategory, Dish, Reservation
from django.utils.safestring import mark_safe

admin.site.register(DishCategory)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    '''
    Admin configuration for the Dish model.

    Attributes:
        prepopulated_fields (dict): Automatically generates the 'slug' based on the 'name' field.
        list_display (tuple): Specifies the fields displayed in the admin list view.
        list_editable (tuple): Allows editing of specified fields directly from the admin list view.
        search_fields (tuple): Enables search functionality based on specified fields.
        list_filter (tuple): Provides filtering options in the admin list view.

    Methods:
        photo_src_tag(obj): Custom method to display the dish photo as a thumbnail in the admin list view.
    '''
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'category', 'name', 'price', 'is_visible', 'photo_src_tag')
    list_editable = ('name', 'category', 'price', 'is_visible',)
    search_fields = ('name',)
    list_filter = ('category', 'price', 'is_visible',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}'width='50' height='50' style='object-fit: cover;'>")

    photo_src_tag.short_description = 'Dish photo'


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    '''
    Admin configuration for ContactMessage model

    Attributes:
        list_display: tuple;
        list_editable: tuple;

    Note:
        The 'is_processed' field is included in 'list_editable', allowing direct editing in admin.
    '''
    list_display = ('name', 'email', 'phone', 'date', 'time', 'people', 'created_at', 'updated_at', 'is_processed')
    list_editable = ('is_processed',)
