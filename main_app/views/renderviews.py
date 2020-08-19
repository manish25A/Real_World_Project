from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect


def PageNotFound(request):
    return render(request, '404.html')


def index(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def AdminDashboard(request):
    return render(request, 'AdminDashboard.html')

def CustomerDashboard(request):
    return render(request, 'CustomerDashboard.html')


def login(request):
    return render(request, 'login.html')


def about(request):
    return render(request, 'aboutus.html')


def professional(request):
    return render(request, 'professionals.html')


def contactpage(request):
    return render(request, 'contact.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def candidatelogin(request):
    try:
        request.session['email'] = request.POST['email']
        request.session['password'] = request.POST['password']
        return redirect('/')
    except ObjectDoesNotExist:
        messages.warning(request, "Please Enter valid email or  password.")
        return redirect('/login')
        pass
