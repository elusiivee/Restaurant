from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import MainMenueItems, Footer, Slider, Chefs, Customers, Progress


@admin.register(MainMenueItems)
class MainMenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'is_visible', 'order')
    list_editable = ('is_visible', 'order',)
@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'photo_src_tag', 'is_visible')
    list_editable = ('is_visible',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    photo_src_tag.short_description = 'Customer photo'


admin.site.register(Footer)
admin.site.register(Slider)
@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'photo_src_tag', 'is_visible', )
    list_editable = ('is_visible',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}'width='50' height='50' style='object-fit: cover;'>")

    photo_src_tag.short_description = 'Customer photo'


def photo_src_tag(self, obj):
    if obj.photo:
        return mark_safe(f"<img src='{obj.photo.url}'width='50' height='50' style='object-fit: cover;'>")


photo_src_tag.short_description = 'Dish photo'

admin.site.register(Progress)
