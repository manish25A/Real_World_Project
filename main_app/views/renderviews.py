from django.shortcuts import render

# main pages
from main_app.models.models import jobpostmodel, Provider


def index(request):
    return render(request, 'mainpages/home.html')


def error_404(request):
    return render(request, 'mainpages/404.html')


def aboutus(request):
    return render(request, 'mainpages/aboutus.html')


def contactpage(request):
    return render(request, 'mainpages/contact.html')


def jobspage(request):
    jobspost = jobpostmodel.objects.all()
    return render(request, 'mainpages/Jobs.html', {'jobs_post': jobspost})


# providers

def providerdashboard(request, id):
    dash = Provider.objects.get(compname=id)
    return render(request, 'providers/providersdash.html', {'dash': dash})


def jobstable(request):
    return render(request, 'providers/employeetable.html')


def jobpost(request):
    return render(request, 'providers/jobpost.html')


def providerlogin(request):
    return render(request, 'providers/providerslogin.html')


def professional(request):
    return render(request, 'providers/professionals.html')


# seekers

def seekerslogin(request):
    return render(request, 'seekers/loginjobseeker.html')


def jobsform(request):
    return render(request, 'seekers/JobsForm.html')


def seekerapply(request):
    return render(request, 'seekers/seekersapply.html')
