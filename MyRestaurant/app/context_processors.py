from .models import MainMenueItems, Footer, Slider, Chef

def main_menu_items(request):
    items = MainMenueItems.objects.filter(is_visible=True)
    return {'main_menu': items}

def slide_item(request):
    items = Slider.objects.filter(is_visible=True)
    return {'slide_item': items}

def chef_item(request):
    items = Chef.objects.filter(is_visible=True)
    return {'chef_item': items}

def footer_items(request):
    items = Footer.objects.first()
    return {'footer_item': items}