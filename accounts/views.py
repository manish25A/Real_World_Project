from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, RedirectView

from accounts.forms import *
from accounts.models import User


# rendering and saving signup page for employee
class RegisterEmployeeView(CreateView):
    # defining models, forms and template
    model = User
    form_class = EmployeeRegistrationForm

    template_name = 'employees/seekersignup.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    # saving the form data if the  form is valid
    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return redirect('accounts:login')
        else:
            return render(request, 'employees/seekersignup.html', {'form': form})


# rendering and saving signup page for employer
class RegisterEmployerView(CreateView):
    model = User
    form_class = EmployerRegistrationForm
    template_name = 'employers/providerssignup.html'
    success_url = '/'

    # checking if some user is logged in or not
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    # posting the save data after validating
    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return redirect('accounts:login')
        else:
            return render(request, 'employers/providerssignup.html', {'form': form})


# loggin in with email and password
class LoginView(FormView):
    """
         login as a user with an email and password
    """
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if 'next' in self.request.GET and self.request.GET['next'] != '':
            return self.request.GET['next']
        else:
            return self.success_url

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(RedirectView):
    """
   logout view
    """
    url = '/login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)
