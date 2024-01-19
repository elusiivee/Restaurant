from django.test import TestCase
from app.models import MainMenueItems, Slider, About, Progress, Services, Chefs, Customers, Footer


class MainMenueItemsTest(TestCase):
    '''
    Class MainMenueItemsTest testing model MainMenueItems

    Methods:
        setUp(self): Creates a sample menu item for testing.

        test_menu_item_attributes(self): Tests the attributes of the menu item created in setUp.
    '''

    def setUp(self):
        MainMenueItems.objects.create(title='Item1', slug='Item1', is_manager='False', is_visible='True', order='1')

    def test_menu_item_attributes(self):
        menu_item = MainMenueItems.objects.get(title="Item1")

        self.assertEqual(menu_item.title, "Item1")
        self.assertEqual(menu_item.slug, "Item1")
        self.assertFalse(menu_item.is_manager)
        self.assertTrue(menu_item.is_visible)
        self.assertEqual(menu_item.order, 1)


class SliderTest(TestCase):
    '''
    Class SliderTest testing model Slider

    Methods:
        setUp(self): Creates a sample slider item for testing.

        test_slider_item_attributes(self): Tests the attributes of the menu item created in setUp.
    '''

    def setUp(self):
        Slider.objects.create(title='Item1', photo='Item1', is_visible='True')

    def test_slider_item_attributes(self):
        slider_item = Slider.objects.get(title="Item1")

        self.assertEqual(slider_item.title, "Item1")
        self.assertTrue(slider_item.is_visible)


class AboutTest(TestCase):
    '''
    Class AboutTest testing model About

    Methods:
        setUp(self): Creates a sample about item for testing.

        test_about_item_attributes(self): Tests the attributes of the menu item created in setUp.
    '''

    def setUp(self):
        About.objects.create(title='Item1', description='Description1')

    def test_about_item_attributes(self):
        about_item = About.objects.get(title="Item1")

        self.assertEqual(about_item.title, "Item1")
        self.assertEqual(about_item.description, "Description1")


class ProgressTest(TestCase):
    '''
    Class ProgressTest testing model Progress

    Methods:
        setUp(self): Creates a sample progress item for testing.

        test_progress_item_attributes(self): Tests the attributes of the menu item created in setUp.
    '''

    def setUp(self):
        Progress.objects.create(title='Item1', value=75.5, is_visible=True)

    def test_progress_item_attributes(self):
        progress_item = Progress.objects.get(title="Item1")

        self.assertEqual(progress_item.title, "Item1")
        self.assertEqual(progress_item.value, 75.5)
        self.assertTrue(progress_item.is_visible)


class ServicesTest(TestCase):
    '''
    Class ServicesTest testing model Services

    Methods:
        setUp(self): Creates a sample service item for testing.

        test_services_item_attributes(self): Tests the attributes of the menu item created in setUp.
    '''

    def setUp(self):
        Services.objects.create(title='Item1', description='Description1', is_visible=True)

    def test_services_item_attributes(self):
        services_item = Services.objects.get(title="Item1")

        self.assertEqual(services_item.title, "Item1")
        self.assertEqual(services_item.description, "Description1")
        self.assertTrue(services_item.is_visible)


class ChefsTest(TestCase):
    '''
    Class ChefsTest testing model Chefs

    Methods:
        setUp(self): Creates a sample chef item for testing.

        test_chefs_item_attributes(self): Tests the attributes of the menu item created in setUp.
    '''

    def setUp(self):
        Chefs.objects.create(
            name='Item1', status='Status1', description='Description1',
            twitter_link='https://twitter.com/chef1', facebook_link='https://www.facebook.com/chef1',
            instagram_link='https://www.instagram.com/chef1',
            is_visible=True,
        )

    def test_chefs_item_attributes(self):
        chefs_item = Chefs.objects.get(name="Item1")

        self.assertEqual(chefs_item.name, "Item1")
        self.assertEqual(chefs_item.status, "Status1")
        self.assertEqual(chefs_item.description, "Description1")
        self.assertEqual(chefs_item.twitter_link, 'https://twitter.com/chef1')
        self.assertEqual(chefs_item.facebook_link, 'https://www.facebook.com/chef1')
        self.assertEqual(chefs_item.instagram_link, 'https://www.instagram.com/chef1')
        self.assertTrue(chefs_item.is_visible)


class CustomersTest(TestCase):
    '''
    Class CustomersTest testing model Customers

    Methods:
        setUp(self): Creates a sample customer item for testing.

        test_customers_item_attributes(self): Tests the attributes of the menu item created in setUp.
    '''

    def setUp(self):
        Customers.objects.create(
            name='Item1', comment='Comment1', is_visible=True,
        )

    def test_customers_item_attributes(self):
        customers_item = Customers.objects.get(name="Item1")

        self.assertEqual(customers_item.name, "Item1")
        self.assertEqual(customers_item.comment, "Comment1")
        self.assertTrue(customers_item.is_visible)


class FooterTest(TestCase):
    '''
    Class FooterTest testing model Footer

    Methods:
        setUp(self): Creates a sample footer item for testing.

        test_footer_item_attributes(self): Tests the attributes of the menu item created in setUp.
    '''

    def setUp(self):
        Footer.objects.create(
            title='Item1', opening_hours='Mon-Fri: 9am-6pm, Sat-Sun: 8am-4pm', newsletter='New news1',
            twitter_link='https://twitter.com/chef1', facebook_link='https://www.facebook.com/chef1',
            instagram_link='https://www.instagram.com/chef1',
            copyright_text="All rights reserved.",
        )

    def test_footer_item_attributes(self):
        footer_item = Footer.objects.get(title="Item1")

        self.assertEqual(footer_item.title, "Item1")
        self.assertEqual(footer_item.opening_hours, "Mon-Fri: 9am-6pm, Sat-Sun: 8am-4pm")
        self.assertEqual(footer_item.newsletter, "New news1")
        self.assertEqual(footer_item.twitter_link, 'https://twitter.com/chef1')
        self.assertEqual(footer_item.facebook_link, 'https://www.facebook.com/chef1')
        self.assertEqual(footer_item.instagram_link, 'https://www.instagram.com/chef1')
        self.assertTrue(footer_item.copyright_text, "All rights reserved.")
