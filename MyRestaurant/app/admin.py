from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import MainMenueItems, Footer, Slider, Chefs, Customers, Progress, About, Services


@admin.register(About)
class AboutItemAdmin(admin.ModelAdmin):
    '''
    Admin configuration for About model

    Attributes:
        list_display: tuple;
        list_editable: tuple;

    Note:
        The 'description' field is included in 'list_editable', allowing direct editing in admin.

    '''
    list_display = ('title', 'description',)
    list_editable = ('description',)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    '''
        Admin configuration for Services model

        Attributes:
            list_display: tuple;
            list_editable: tuple;

        Note:
            'description' and 'is_visible' field is included in 'list_editable', allowing direct editing in admin.
            'photo_src_tag' is returned from the function 'def photo_src_tag()' for allowing to display photos in admin
    '''
    list_display = ('title', 'description', 'photo_src_tag', 'is_visible')
    list_editable = ('description', 'is_visible',)

    def photo_src_tag(self, obj):
        '''
        Generate HTML-teg img to display photo in admin
        :param obj:
        '''
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    photo_src_tag.short_description = 'Customer photo'


@admin.register(MainMenueItems)
class MainMenuItemAdmin(admin.ModelAdmin):
    '''
        Admin configuration for Services model

        Attributes:
            list_display: tuple;
            list_editable: tuple;

        Note:
            prepopulated_fields (dict): Automatically creates the 'slug' field based on the 'title'.
            'order' and 'is_visible' field is included in 'list_editable', allowing direct editing in admin.


    '''
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'is_visible', 'order')
    list_editable = ('is_visible', 'order',)


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    '''
        Admin configuration for Services model

        Attributes:
            list_display: tuple;
            list_editable: tuple;

        Note:
            'description' and 'is_visible' fields is included in 'list_editable', allowing direct editing in admin.
            'photo_src_tag' is returned from the function 'def photo_src_tag()' for allowing to display photos in admin
    '''
    list_display = ('name', 'comment', 'photo_src_tag', 'is_visible')
    list_editable = ('is_visible',)

    def photo_src_tag(self, obj):
        '''
        Generate HTML-teg img to display photo in admin
        :param obj:
        '''
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    photo_src_tag.short_description = 'Customer photo'


admin.site.register(Footer)
admin.site.register(Slider)


@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    '''
        Admin configuration for Services model

        Attributes:
            list_display: tuple;
            list_editable: tuple;

        Note:
            The 'is_visible' field is included in 'list_editable', allowing direct editing in admin.
            'photo_src_tag' is returned from the function 'def photo_src_tag()' for allowing to display photos in admin
    '''
    list_display = ('name', 'status', 'photo_src_tag', 'is_visible',)
    list_editable = ('is_visible',)

    def photo_src_tag(self, obj):
        '''
        Generate HTML-teg img to display photo in admin
        :param obj:
        '''
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}'width='50' height='50' style='object-fit: cover;'>")

    photo_src_tag.short_description = 'Customer photo'


admin.site.register(Progress)
