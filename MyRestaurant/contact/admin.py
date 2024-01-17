from django.contrib import admin
from .models import ContactInfo, ContactMessage

# registration Contactinfo to admin

admin.site.register(ContactInfo)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    '''
        Admin configuration for ContactMessage model

        Attributes:
            list_display: tuple;
            list_editable: tuple;

        Note:
            The 'is_processed' field is included in 'list_editable', allowing direct editing in admin.
        '''
    list_display = ('name', 'email', 'subject', 'message', 'is_processed', 'created_at')
    list_editable = ('is_processed',)
