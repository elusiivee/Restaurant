from django.contrib import admin
from .models import MainMenueItems, Footer, Slider, Chef


@admin.register(MainMenueItems)
class MainMenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','slug', 'is_visible', 'order')
    list_editable = ('is_visible', 'order',)

admin.site.register(Footer)
admin.site.register(Slider)
admin.site.register(Chef)