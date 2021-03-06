from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView

from main_app.forms.forms import ApplyJobForm, ContactForm
from main_app.models.models import Job, Applicant


# rendering data in homepage
class HomeView(ListView):
    model = Job
    template_name = 'mainpages/home.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return self.model.objects.all()[:20]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trendings'] = self.model.objects.filter(created_at__month=timezone.now().month)[:3]
        return context


# searchview on the basis of  location and postion
class SearchView(ListView):
    model = Job
    template_name = 'mainpages/search.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return self.model.objects.filter(location__contains=self.request.GET['location'],
                                         title__contains=self.request.GET['position'])


# showing the jobs data
class JobListView(ListView):
    model = Job
    template_name = 'mainpages/Jobs.html'
    context_object_name = 'jobs'
    paginate_by = 8


# details about job
class JobDetailsView(DetailView):
    model = Job
    template_name = 'mainpages/jobdetails.html'
    context_object_name = 'job'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        obj = super(JobDetailsView, self).get_object(queryset=queryset)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # raise error
            raise Http404("Job doesn't exists")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


# job apply view
class ApplyJobView(CreateView):
    model = Applicant
    form_class = ApplyJobForm
    slug_field = 'job_id'
    slug_url_kwarg = 'job_id'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.info(self.request, 'Successfully applied for the job!')
            return self.form_valid(form)
        else:
            return HttpResponseRedirect(reverse_lazy('home'))

    def get_success_url(self):
        return reverse_lazy('main:jobs-detail', kwargs={'id': self.kwargs['job_id']})

    def form_valid(self, form):
        # check if user already applied
        applicant = Applicant.objects.filter(user_id=self.request.user.id, job_id=self.kwargs['job_id'])
        if applicant:
            messages.info(self.request, 'You already applied for this job')
            return HttpResponseRedirect(self.get_success_url())
        # save applicant
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


# rendering normal pages
def contactpage(request):
    return render(request, 'mainpages/contact.html')


# saving the contact data which is sent to the developers
def contactsave(request):
    form = ContactForm(request.POST, request.FILES)
    form.save()
    return redirect(reverse_lazy("main:contactpage"))


# deleting job
def jobdelete(request, id):
    user = Job.objects.get(id=id)
    user.delete()
    return redirect('main:employer-dashboard')


# rendering about us page
def aboutus(request):
    return render(request, 'mainpages/aboutus.html')
