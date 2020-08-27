from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.defaults import page_not_found
from django.shortcuts import render, redirect

from main_app.models.models import jobpostmodel


# main pages
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

def providerdashboard(request):
    return render(request, 'providers/providersdash.html')


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


def seekerdash(request):
    return render(request, 'seekers/userdash.html')


def appliedlist(request):
    return render(request, 'seekers/usertable.html')


def apply(request):
    return render(request, 'seekers/seekersapply.html')
