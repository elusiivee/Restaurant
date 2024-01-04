from django.urls import path
from .views import Blog_view

app_name='blog'

urlpatterns = [
    path('', Blog_view.as_view(), name='blog_page'),
]


