from django.urls import path
from .views import Contact_view

app_name = 'contact'

urlpatterns = [
    path('', Contact_view.as_view(), name='contact_page'),

]
