from django.shortcuts import render
from .models import Dish, DishCategory
# Create your views here.
def main(request):
    category = DishCategory.objects.filter(is_visible=True)
    dish = Dish.objects.filter(is_visible=True)
    context = {
        'categories':category,
        'dishes' : dish,
    }
    return render(request, 'main_file.html', context=context)

