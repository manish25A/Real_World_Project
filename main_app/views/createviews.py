from django.shortcuts import render, redirect

# importing from forms and views of another app
# from admin_app.views.views import adminpage
from main_app.forms.forms import CandidateForm, ContactForm


def candidatecreate(request):
    if request.method == "POST":
        candidateform = CandidateForm(request.POST)
        candidateform.save()
        return redirect('login')
    candidate_create = CandidateForm()
    return render(request, 'login.html', {'candidateCreate': candidate_create})


def contactform(request):
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        contactform.save()
        return redirect('contactpage')
    contactform = ContactForm()
    return render(request, 'contact.html', {'contactform': contactform})
