from django.contrib import admin
from .models import MainMenueItems, Footer


@admin.register(MainMenueItems)
class MainMenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','slug', 'is_visible', 'order')
    list_editable = ('is_visible', 'order',)

admin.site.register(Footer)