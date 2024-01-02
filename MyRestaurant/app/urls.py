from django.urls import path
from .views import menu

app_name = 'app'

urlpatterns = [
    path('', menu, name='menu'),


]