from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from main_app.views import createviews, renderviews

urlpatterns = [
    # render urls
    path('', renderviews.index, name='index'),
    path("404", renderviews.error_404, name='404'),
    path('aboutus', renderviews.aboutus, name='aboutus'),
    path('contactpage', renderviews.contactpage, name='contactpage'),

    path('jobspage', renderviews.jobspage, name='jobspage'),

    # employer
    path('employer', renderviews.professional, name='employer'),
    path('employer/dash/<str:id>', renderviews.providerdashboard, name='providerdash'),
    path('providerlogin', createviews.providerlogin, name='providerlogin'),

    path('employer/jobpost', renderviews.jobpost, name='jobpost'),
    path('employer/login', renderviews.providerlogin, name='employerlogin'),
    path('employer/jobs', renderviews.jobstable, name='job_lists'),
    path('providersignup', createviews.providersignup, name='providersignup'),

    path('professional', renderviews.professional, name='professional'),

    # seekers
    path('seekers/login', renderviews.seekerslogin, name='seekerslogin'),
    path("seekers/dash/<str:id>", createviews.seekerdash, name='seekerdash'),
    path('seekers/apply', renderviews.seekerapply, name='seekerapply'),
    path('candidatelogin', createviews.candidatelogin, name='candidatelogin'),
    path('seekers/data/<str:id>', createviews.appliedlist, name='appliedlist'),

    # create urls

    path('contactpage/save', createviews.contactformdata, name='contactpagesave'),
    path('seekers/signup', createviews.jobseekersignup, name='seekersignup'),
    path('jobpostformdata', createviews.jobpostformdata, name='jobpostformdata'),

]
urlpatterns += staticfiles_urlpatterns()
