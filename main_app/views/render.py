from django.shortcuts import render
from django.views.generic import CreateView

from main_app.forms.forms import ContactForm


def contactpage(request):
    return render(request, 'mainpages/contact.html')
def aboutpage(request):
    return render(request, 'mainpages/aboutus.html')
