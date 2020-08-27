from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from main_app.models.models import Candidate
from main_app.forms.forms import CandidateTable, ContactForm, jobpostform
from django.contrib import messages


def candidatecreate(request):
    if request.method == "POST":
        candidateform = CandidateTable(request.POST)
        candidateform.save()
        return redirect('login')
    else:
        candidateform = CandidateTable()
    return render(request, 'mainpages/login.html', {'candidateCreate': candidateform})


def contactform(request):
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        contactform.save()
        return redirect('contactpage')
    contactform = ContactForm()
    return render(request, 'mainpages/contact.html', {'contactform': contactform})


def jobpostformdata(request):
    if request.method == "POST":
        jobpost = jobpostform(request.POST)
        jobpost.save()
        return redirect('contactpage')
    jobpost = jobpostform()
    return render(request, 'mainpages/contact.html', {'jobpost': jobpost})



def loginValidate(request):
    try:
        # storing email and password in session
        request.session['Email'] = request.POST["Email"]
        request.session['Password'] = request.POST["Password"]
        # admin login
        if request.session['Email'] == "admin@gmail.com":
            if request.session['Password'] == "admin123":
                return redirect('/adminpage/')
        else:
            # candidate login
            customers = Candidate.objects.get()
            return redirect("/dashboard/'")
    except:
        messages.warning(request, "Invalid Username or Password")
        return redirect('/index/')

##

def candidatelogin(request):
    try:
        request.session['email'] = request.POST['email']
        request.session['password'] = request.POST['password']
        return redirect('/dashboard')
    except ObjectDoesNotExist:
        messages.warning(request, "Please Enter valid email or  password.")
        return redirect('/login')
        pass
