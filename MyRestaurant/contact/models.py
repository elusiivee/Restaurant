from django.db import models


class ContactInfo(models.Model):
    '''
    Model representing contact info.

    Fields:
        address (CharField): Displaying address on website.
        phone (CharField): Displaying phone on website.
        email (EmailField): Displaying email on website.
    '''
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self) -> str:
        return 'Contact info'


class ContactMessage(models.Model):
    '''
    Model representing contact messages sent by customers to the admin.

    Fields:
        name (CharField): Sender's name.
        email (EmailField): Sender's email address.
        subject (CharField): Subject of the contact message.
        message (TextField): Content of the contact message.
        is_processed (BooleanField): Indicates whether the message has been processed by the admin.
        created_at (DateTimeField): Date and time when the message was created (auto-generated).
    '''
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.email}"

    class Meta:
        ordering = ('-created_at',)
