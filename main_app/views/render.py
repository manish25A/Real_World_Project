from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main_app.forms.forms import ContactForm


class contactpage(CreateView):
    template_name = 'mainpages/contact.html'
    form_class = ContactForm
    extra_context = {
        'title': 'Contact Page'
    }
    success_url = reverse_lazy('job:contactpage')

<<<<<<< Updated upstream
def contactpage(request):
    return render(request, 'mainpages/contact.html')
def aboutpage(request):
    return render(request, 'mainpages/aboutus.html')
=======
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(contactpage, self).form_valid(form)
>>>>>>> Stashed changes

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def aboutus(request):
    return render(request, 'mainpages/aboutus.html')
