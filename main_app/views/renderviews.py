from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views.defaults import page_not_found
from django.shortcuts import render, redirect


def error_404(request):
    return render(request, 'mainpages/404.html')


def index(request):
    try:
        return render(request, 'mainpages/home.html')
    except page_not_found:
        return redirect(request, error_404)


def dashboard(request):
    return render(request, 'mainpages/dashboard.html')


def AdminDashboard(request):
    return render(request, 'providers/admindash.html')


def CreateAdmin(request):
    return render(request, 'providers/createAdmin.html')


def ViewAdmin(request):
    return render(request, 'providers/adminView.html')


def UpdateAdmin(request):
    return render(request, 'providers/editAdmin.html')


def DeleteAdmin(request):
    return render(request, 'providers/editAdmin.html')


def CustomerDashboard(request):
    return render(request, 'professionals/customerdash.html')


def CreateCustomer(request):
    return render(request, 'professionals/createCustomer.html')


def ViewCustomer(request):
    return render(request, 'professionals/customerView.html')


def UpdateCustomer(request):
    return render(request, 'professionals/editCustomer.html')


def DeleteCustomer(request):
    return render(request, 'professionals/editCustomer.html')


def login(request):
    return render(request, 'mainpages/login.html')


def about(request):
    return render(request, 'mainpages/aboutus.html')


def professional(request):
    return render(request, 'providers/professionals.html')


def contactpage(request):
    return render(request, 'mainpages/contact.html')

def jobspage(request):
    return render(request, 'mainpages/Jobs.html')


def aboutus(request):
    return render(request, 'mainpages/aboutus.html')


def candidatelogin(request):
    try:
        request.session['email'] = request.POST['email']
        request.session['password'] = request.POST['password']
        return redirect('/dashboard')
    except ObjectDoesNotExist:
        messages.warning(request, "Please Enter valid email or  password.")
        return redirect('/login')
        pass
