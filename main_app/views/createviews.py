from django.shortcuts import render, redirect

from main_app.forms.forms import seekerform, seekerapplyform, jobpostform, contactform, providerform
from main_app.models.models import Seeker,Provider


def appliedlist(request, id):
    # appliedtable = jobpostmodel.objects.get(seekerusername=id)
    return render(request, 'seekers/usertable.html', {'appliedtable': appliedtable})


def jobseekersignup(request):
    if request.method == "POST":
        seekerdata = seekerform(request.POST or None)
        seekerdata.save()
        return redirect('seekerslogin')


def providersignup(request):
    if request.method == "POST":
        providerdata = providerform(request.POST or None)
        providerdata.save()
        return redirect('employer/login')


def jobapply(request):
    if request.method == "POST":
        applydata = seekerapplyform(request.POST or None)
        applydata.save()
        return redirect('seekerslogin')


def seekerdash(request, id):
    dash = Seeker.objects.get(seekerusername=id)
    return render(request, 'seekers/userdash.html', {'dash': dash})


def contactformdata(request):
    if request.method == "POST":
        contactformdata = contactform(request.POST or None)
        contactformdata.save()
        return redirect('contactpage')


def jobpostformdata(request):
    if request.method == "POST":
        jobpost = jobpostform(request.POST)
        jobpost.save()
        return redirect('contactpage')
    jobpost = jobpostform()
    return render(request, 'mainpages/contact.html', {'jobpost': jobpost})


def candidatelogin(request):
    request.session['seekeremail'] = request.POST['seekeremail']
    request.session['seekerpassword'] = request.POST['seekerpassword']
    loginform = Seeker.objects.get(seekeremail=request.session['seekeremail'])
    user = loginform.seekerusername
    return redirect("/seekers/dash/" + user + "")


def providerlogin(request):
    request.session['email'] = request.POST['email']
    request.session['password'] = request.POST['password']
    loginform = Provider.objects.get(email=request.session['email'])
    user = loginform.compname
    return redirect("/employer/dash/" + user + "")
