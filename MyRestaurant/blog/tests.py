from django.test import TestCase
from .models import Blog


class BlogTest(TestCase):
    '''
    Class BlogTest testing model Blog

    Methods:
        setUp(self): Creates a sample blog item for testing.

        test_blog_item_attributes(self): Tests the attributes of the blog item created in setUp.
    '''

    def setUp(self):
        Blog.objects.create(title='Item1', content='Content1', is_visible=True)

    def test_blog_item_attributes(self):
        blog_item = Blog.objects.get(title="Item1")

        self.assertEqual(blog_item.title, "Item1")
        self.assertEqual(blog_item.content, "Content1")
        self.assertTrue(blog_item.is_visible)
