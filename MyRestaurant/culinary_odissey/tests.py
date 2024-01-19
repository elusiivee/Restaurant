from django.test import TestCase
from decimal import Decimal
from .forms import ReservationForm

from .models import DishCategory, Dish


class ReservationFormTest(TestCase):
    '''
    Class for testing forms from ReservationForm.
    '''

    def test_valid_data(self):
        form = ReservationForm(data={
            'name': 'Mr Test',
            'email': 'test@gmail.com',
            'phone': '124124124',
            'date': '2023-10-10',
            'time': '17:00',
            'people': '2',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = ReservationForm(data={
            'name': 'Mr Test',
            'email': 'invalid',
            'phone': 'invalid',
            'date': 'invalid',
            'time': 'invalid',
            'people': 'invalid',
        })
        self.assertFalse(form.is_valid())
        print(form.errors)  # Print the form errors


class DishCategoryTest(TestCase):
    '''
    Class DishCategoryTest testing model DishCategory

    Methods:
        setUp(self): Creates a sample dish_category item for testing.

        test_dish_category_item_attributes(self): Tests the attributes of the dish_category item created in setUp.
    '''

    def setUp(self):
        DishCategory.objects.create(name='Item1', order=1, is_visible=True)

    def test_dish_category_item_attributes(self):
        dish_category = DishCategory.objects.get(name="Item1")

        self.assertEqual(dish_category.name, "Item1")
        self.assertEqual(dish_category.order, 1)
        self.assertTrue(dish_category.is_visible)


class DishTest(TestCase):
    '''
    Class DishTest testing model Dish

    Methods:
        setUp(self): Creates a sample dish item for testing.

        test_dish_item_attributes(self): Tests the attributes of the dish item created in setUp.
    '''

    def setUp(self):
        # Create a DishCategory first
        category = DishCategory.objects.create(name='Category1', order=1)

        # Now create a Dish instance with a valid category
        Dish.objects.create(name='Item1', slug='Item1', ingredients='Ingredients1', price=Decimal('99.99'),
                            is_visible=True, order=1, category=category)

    def test_dish_item_attributes(self):
        dish_item = Dish.objects.get(name="Item1")

        self.assertEqual(dish_item.name, "Item1")
        self.assertEqual(dish_item.slug, "Item1")
        self.assertEqual(dish_item.ingredients, "Ingredients1")
        self.assertEqual(dish_item.price, Decimal('99.99'))
        self.assertTrue(dish_item.is_visible)
        self.assertEqual(dish_item.order, 1)
