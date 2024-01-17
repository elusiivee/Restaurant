from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    '''
    Admin configuration for Blog model

    Attributes:
        list_display: tuple;
        list_editable: tuple;

    Note:
        The 'is_visible' field is included in 'list_editable', allowing direct editing in admin.
        'photo_src_tag' is returned from the function 'def photo_src_tag()' for allowing to display photos in admin.
    '''
    list_display = ('title', 'photo_src_tag', 'updated_at', 'is_visible',)
    list_editable = ('is_visible',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}'width='50' height='50' style='object-fit: cover;'>")

    photo_src_tag.short_description = 'Blog photo'
