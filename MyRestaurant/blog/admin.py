from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Blog


@admin.register(Blog)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo_src_tag', 'updated_at', 'is_visible',)
    list_editable = ('is_visible',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}'width='50' height='50' style='object-fit: cover;'>")

    photo_src_tag.short_description = 'Blog photo'
