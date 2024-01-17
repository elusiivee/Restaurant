from django.views.generic import TemplateView
from .models import Blog

class Blog_view(TemplateView):
    '''
    View for rendering the blog page.

    Attributes:
        template_name (str): HTML template used for rendering the blog page.

    Methods:
        get_context_data(**kwargs): Retrieves context data for rendering the template.
    '''

    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_info'] = Blog.objects.filter(is_visible=True)
        return context