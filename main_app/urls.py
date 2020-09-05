from django.urls import path, include

from main_app.views import home, employer
from main_app.views.employer import *
from main_app.views.home import *
from main_app.views.render import *

app_name = "main"

urlpatterns = [
    path('contactpage', contactpage, name='contactpage'),
    path('contactsave', contactsave, name='contactsave'),
    path('aboutus', home.aboutus, name='aboutus'),
    path('job/delete/<int:id>', home.jobdelete, name='job-delete'),

    path('', HomeView.as_view(), name='home'),
    path('search', SearchView.as_view(), name='search'),
    path('employer/dashboard/', include([
        path('', DashboardView.as_view(), name='employer-dashboard'),
        path('all-applicants', ApplicantsListView.as_view(), name='employer-all-applicants'),
        path('applicants/<int:job_id>', ApplicantPerJobView.as_view(), name='employer-dashboard-applicants'),

        path('mark-filled/<int:job_id>', filled, name='job-mark-filled'),
    ])),

    path('apply-job/<int:job_id>', ApplyJobView.as_view(), name='apply-job'),
    path('jobs', JobListView.as_view(), name='jobs'),
    path('jobs/<int:id>', JobDetailsView.as_view(), name='jobs-detail'),
    path('employer/jobs/create', JobCreateView.as_view(), name='employer-jobs-create'),
]
