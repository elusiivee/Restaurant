from django.shortcuts import render, redirect
from .models import Dish, DishCategory
from django.views.generic import TemplateView
from .forms import ReservationForm
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.urls import reverse

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
    template_name = './main_file.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = DishCategory.objects.filter(is_visible=True)
        dish = Dish.objects.filter(is_visible=True)
        context['categories'] = categories
        context['dishes'] = dish
        context['reservation_form'] = ReservationForm()
        return context

    def post(self, request, *args, **kwargs):
        reservation_form = ReservationForm(request.POST)

        if reservation_form.is_valid():
            reservation_form.save()
            messages.success(request, 'Reservation done')
            return redirect('odyssey:home')

        context = self.get_context_data(**kwargs)
        context['reservation_form'] = ReservationForm()
        messages.error(request,'Errors in form Reservation')
        return render(request, 'main_file.html', context=context)



class Menu(TemplateView):
    template_name = './menu_second.html'

    def get_context_data(self, **kwargs):
        context = self.get_context_data(**kwargs)
        categories = DishCategory.objects.filter(is_visible=True)
        dish = Dish.objects.filter(is_visible=True)
        context['categories'] = categories
        context['dishes'] = dish
        context['reservation_form'] = ReservationForm()
        return context

    def post(self, request, *args, **kwargs):
        reservation_form = ReservationForm(request.POST)

        if reservation_form.is_valid():
            reservation_form.save()
            messages.success(request, 'Reservation done')
            return redirect('odyssey:home')

        context = self.get_context_data(**kwargs)
        context['reservation_form'] = ReservationForm()
        messages.error(request,'Errors in form eEservation')
        return render(request, 'menu.html', context=context)