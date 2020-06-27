from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

# importing from forms and views of another app
#from admin_app.views.views import adminpage
from main_app.forms.forms import CandidateSign


def index(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def candidatecreate(request):
    if request.method == "POST":
        candidateform = CandidateSign(request.POST)
        candidateform.save()
        return redirect('login')
    candidate_create = CandidateSign()
    return render(request, 'login.html', {'candidateCreate': candidate_create})


def candidatelogin(request):
    try:
        request.session['email'] = request.POST['email']
        request.session['password'] = request.POST['password']
        return redirect('/')
    except ObjectDoesNotExist:
        messages.warning(request, "Please Enter valid email or  password.")
        return redirect('/login')
        pass
