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
    return render(request, 'admindash.html')

def CreateAdmin(request):
    return render(request, 'createAdmin.html')

def ViewAdmin(request):
    return render(request, 'adminView.html')

def UpdateAdmin(request):
    return render(request, 'editAdmin.html')

def DeleteAdmin(request):
    return render(request, 'editAdmin.html')



def CustomerDashboard(request):
    return render(request, 'customerdash.html')


def CreateCustomer(request):
    return render(request, 'createCustomer.html')

def ViewCustomer(request):
    return render(request, 'customerView.html')

def UpdateCustomer(request):
    return render(request, 'editCustomer.html')

def DeleteCustomer(request):
    return render(request, 'editCustomer.html')


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
