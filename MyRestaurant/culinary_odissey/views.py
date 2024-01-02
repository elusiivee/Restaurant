from django.shortcuts import render
from .models import Dish, DishCategory
from django.views.generic import TemplateView
from .forms import ReservationForm


# Create your views here.
# def main(request):
#     category = DishCategory.objects.filter(is_visible=True)
#     dish = Dish.objects.filter(is_visible=True)
#     context = {
#         'categories':category,
#         'dishes' : dish,
#     }
#     return render(request, 'main_file.html', context=context)
#
# def menu(request):
#     category = DishCategory.objects.filter(is_visible=True)
#     dish = Dish.objects.filter(is_visible=True)
#     context = {
#         'categories':category,
#         'dishes' : dish,
#     }
#     return render(request, 'menu_second.html', context=context)

class MainPage(TemplateView):
    template_name = 'main_file.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = DishCategory.objects.filter(is_visible=True)
        dish = Dish.objects.filter(is_visible=True)
        context['categories'] = categories
        context['dishes'] = dish
        context['reservation_form'] = ReservationForm()
        return context

    def post(self, request, *args, **kwargs):
        ...


class Menu(TemplateView):
    template_name = 'menu_second.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = DishCategory.objects.filter(is_visible=True)
        dish = Dish.objects.filter(is_visible=True)
        context['categories'] = categories
        context['dishes'] = dish
        context['reservation_form'] = ReservationForm()
        return context

    def post(self, request, *args, **kwargs):
        ...
