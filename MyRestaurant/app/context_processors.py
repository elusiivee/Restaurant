from .models import MainMenueItems, Footer, Slider, Chefs, Customers

def main_menu_items(request):
    items = MainMenueItems.objects.filter(is_visible=True)
    return {'main_menu': items}

def slide_item(request):
    items = Slider.objects.filter(is_visible=True)
    return {'slide_item': items}

def chef_item(request):
    items = Chefs.objects.filter(is_visible=True)
    return {'chef_item': items}

def customer_item(request):
    items = Customers.objects.filter(is_visible=True)
    return {'customer_item': items}

def footer_items(request):
    items = Footer.objects.first()
    return {'footer_item': items}