from django.urls import path
from .views import main, menu



urlpatterns = [
    path('', main, name='home'),
    path('menu/', menu, name='menu'),
]