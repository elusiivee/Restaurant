from django.contrib import admin
from .models import ContactInfo, ContactMessage



admin.site.register(ContactInfo)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'is_processed', 'created_at')
    list_editable = ('is_processed',)
