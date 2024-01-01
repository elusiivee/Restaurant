from .models import MainMenueItems, Footer

def main_menu_items(request):
    items = MainMenueItems.objects.filter(is_visible=True)
    return {'main_menu': items}

def footer_items(request):
    items = Footer.objects.first()
    return {'footer_item': items}