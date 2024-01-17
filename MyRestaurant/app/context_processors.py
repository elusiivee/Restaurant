from .models import MainMenueItems, Footer, Slider, Chefs, Customers, Progress, About, Services


def about_item(request):
    '''
    Retrieve the first 'About' object from the database and add it to the context.

    This function serves as a context processor, making information about the 'About' object
    available in templates.

    :param request: The HTTP request object
    :return dict: A dictionary containing the 'about_item' key with the 'About' object.
    '''
    item = About.objects.first()
    return {'about_item': item}


def main_menu_items(request):
    '''
    Retrieve the all 'MainMenueItems' object with param: (is_visible= True) from the database and add it to the context.

    This function serves as a context processor, making information about the 'MainMenueItems' object
    available in templates.

    :param request: The HTTP request object
    :return dict: A dictionary containing the 'main_item' key with the 'MainMenueItems' object.
    '''
    items = MainMenueItems.objects.filter(is_visible=True)
    return {'main_menu': items}


def slide_item(request):
    '''
    Retrieve the all 'Slider' object with param: (is_visible= True) from the database and add it to the context.

    This function serves as a context processor, making information about the 'Slider' object
    available in templates.

    :param request: The HTTP request object
    :return dict: A dictionary containing the 'slide_item' key with the 'Slider' object.
    '''
    items = Slider.objects.filter(is_visible=True)
    return {'slide_item': items}


def service_item(request):
    '''
    Retrieve the all 'Services' object with param: (is_visible= True) from the database and add it to the context.

    This function serves as a context processor, making information about the 'Services' object
    available in templates.

    :param request: The HTTP request object
    :return dict: A dictionary containing the 'services_item' key with the 'Services' object.
    '''
    items = Services.objects.filter(is_visible=True)
    return {'services_item': items}


def progress_item(request):
    '''
    Retrieve the all 'Progress' object with param: (is_visible= True) from the database and add it to the context.

    This function serves as a context processor, making information about the 'Progress' object
    available in templates.

    :param request: The HTTP request object
    :return dict: A dictionary containing the 'progress_item' key with the 'Progress' object.
    '''
    items = Progress.objects.filter(is_visible=True)
    return {'progress_item': items}


def chef_item(request):
    '''
    Retrieve the all 'Progress' object with param: (is_visible= True) from the database and add it to the context.

    This function serves as a context processor, making information about the 'Progress' object
    available in templates.

    :param request: The HTTP request object
    :return dict: A dictionary containing the 'progress_item' key with the 'Progress' object.
    '''
    items = Chefs.objects.filter(is_visible=True)
    return {'chef_item': items}


def customer_item(request):
    '''
    Retrieve the all 'Customers' object with param: (is_visible= True) from the database and add it to the context.

    This function serves as a context processor, making information about the 'Customers' object
    available in templates.

    :param request: The HTTP request object
    :return dict: A dictionary containing the 'customer_item' key with the 'Customers' object.
    '''
    items = Customers.objects.filter(is_visible=True)
    return {'customer_item': items}


def footer_items(request):
    '''
    Retrieve the first 'Footer' object from the database and add it to the context.

    This function serves as a context processor, making information about the 'Footer' object
    available in templates.

    :param request: The HTTP request object
    :return dict: A dictionary containing the 'footer_item' key with the 'Footer' object.
    '''
    items = Footer.objects.first()
    return {'footer_item': items}
