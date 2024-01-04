from django.urls import path
from .views import MainPage, Menu, Reservation

app_name='odyssey'

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('menu/', Menu.as_view(), name='menu'),
    path('book_a_table/', Reservation.as_view(), name='book_a_table'),
]