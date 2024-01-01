from django.shortcuts import render
from .models import MainMenueItems, Footer
def menu(request):
    categories = MainMenueItems.objects.filter(is_visible=True)
    footer_info = Footer.objects.first()
    return render(request, 'menu.html', {'categories': categories, 'footer_info': footer_info})

