from django.shortcuts import render
from .models import Dish, DishCategory
# Create your views here.
def main(request):
    category = DishCategory.objects.filter(is_visible=True)
    return render(request, 'main_file.html')

def menu(request):
    category = DishCategory.objects.filter(is_visible=True)
    return render(request, 'menu.html')
