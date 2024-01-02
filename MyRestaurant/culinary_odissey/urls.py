from django.urls import path
from .views import MainPage, Menu

app_name='odyssey'

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('menu/', Menu.as_view(), name='menu'),
]