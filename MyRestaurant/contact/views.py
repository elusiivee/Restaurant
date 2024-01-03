from django.shortcuts import render,redirect
from .forms import ContactForm
from django.views.generic import TemplateView
from django.contrib import messages

class Contact_view(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Reservation done')
            return redirect('odyssey:home')

        context = self.get_context_data(**kwargs)
        context['contact_form'] = ContactForm()
        messages.error(request,'Errors in form Contact')
        return render(request, 'contact.html', context=context)
