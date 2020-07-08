from django.shortcuts import render, redirect

from main_app.forms.forms import CandidateForm, ContactForm


def candidatecreate(request):
    candidateform = CandidateForm(request.POST)
    if request.method == "POST":
        if candidateform.is_valid():
            candidateform.save()
        return redirect('login')
    return render(request, 'login.html', {'candidateCreate': candidateform})


def contactform(request):
    if request.method == "POST":
        contactform = ContactForm(request.POST)
        contactform.save()
        return redirect('contactpage')
    contactform = ContactForm()
    return render(request, 'contact.html', {'contactform': contactform})
