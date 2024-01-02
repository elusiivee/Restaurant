from django.contrib import admin
from .models import MainMenueItems, Footer, Slider, Chefs, Customers, Progress


@admin.register(MainMenueItems)
class MainMenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'is_visible', 'order')
    list_editable = ('is_visible', 'order',)
@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment','photo','is_visible')
    list_editable = ('is_visible',)

admin.site.register(Footer)
admin.site.register(Slider)
admin.site.register(Chefs)
admin.site.register(Progress)
