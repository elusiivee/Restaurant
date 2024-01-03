from django.urls import path
from .views import Contact_view

urlpatterns = [
    path('home/', Contact_view.as_view(), name='contact_page'),


]