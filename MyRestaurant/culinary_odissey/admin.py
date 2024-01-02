from django.contrib import admin
from .models import DishCategory, Dish, Reservation
from django.utils.safestring import mark_safe


admin.site.register(DishCategory)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'category', 'name', 'price', 'is_visible', 'photo_src_tag')
    list_editable = ('name', 'category', 'price', 'is_visible',)
    search_fields = ('name',)
    list_filter = ('category','price', 'is_visible',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}'width='50' height='50' style='object-fit: cover;'>")

    photo_src_tag.short_description = 'Dish photo'


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'people', 'created_at', 'updated_at', 'is_processed')
    list_editable = ('is_processed',)
