from django.shortcuts import render, redirect
from mongoengine import Q

from main_app.models.models import Candidate
from main_app.forms.forms import CandidateTable, ContactForm
from django.contrib import messages


def candidatecreate(request):
    if request.method == "POST":
        candidateform = CandidateTable(request.POST)
        candidateform.save()
        return redirect('login')
    else:
        candidateform=CandidateTable()
    return render(request, 'mainpages/login.html', {'candidateCreate': candidateform})


def contactform(request):
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        contactform.save()
        return redirect('contactpage')
    contactform = ContactForm()
    return render(request, 'mainpages/contact.html', {'contactform': contactform})

def loginValidate(request):
    try:
        #storing email and password in session
        request.session['Email'] = request.POST["Email"]
        request.session['Password'] = request.POST["Password"]
        #admin login
        if (request.session['Email'] == "admin@gmail.com"):
            if (request.session['Password'] == "admin123"):
                return redirect('/adminpage/')
        else:
        #candidate login
            customers = Candidate.objects.get(Q(Email=request.session['Email']) & Q(Password=request.session['Password']))
            id = customers.ID
            return redirect("/dashboard/'" + str(id) + "'")
    except:
        messages.warning(request,"Invalid Username or Password")
        return redirect('/index/')