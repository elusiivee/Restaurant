from django.contrib import admin
from .models import ContactInfo, ContactMessage
from django.utils.safestring import mark_safe


admin.site.register(ContactInfo)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'is_processed', 'created_at')
    list_editable = ('is_processed',)
