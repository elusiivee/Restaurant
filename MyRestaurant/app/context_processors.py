from .models import MainMenueItems

def main_menu_items(request):
    items = MainMenueItems.objects.filter(is_visible=True)
    return {'main_menu': items}
