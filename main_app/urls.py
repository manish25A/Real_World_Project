from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from main_app.views import createviews, renderviews

urlpatterns = [
    # render urls
    path('', renderviews.index, name='index'),
    path("404", renderviews.page_not_found, name='404'),
    path('aboutus', renderviews.aboutus, name='aboutus'),
    path('contactpage', renderviews.contactpage, name='contactpage'),
    path('jobspage', renderviews.jobspage, name='jobspage'),

    # employer
    path('employer', renderviews.professional, name='employer'),
    path('employer/dash', renderviews.providerdashboard, name='providerdash'),
    path('employer/jobpost', renderviews.jobpost, name='jobpost'),
    path('employer/login', renderviews.providerlogin, name='employerlogin'),
    path('employer/jobs', renderviews.jobstable, name='job_lists'),
    path('apply', renderviews.apply, name='apply'),

    path('professional', renderviews.professional, name='professional'),

    # seekers
    path('seekers/login', renderviews.seekerslogin, name='seekerslogin'),
    path('seekers/dash', renderviews.seekerdash, name='seekerdash'),
    # create urls
    path('contactsave', createviews.contactform, name='contactsave'),
    path('candidatecreate', createviews.candidatecreate, name='candidatecreate'),
    path('jobpostformdata', createviews.jobpostformdata, name='jobpostformdata'),

]
urlpatterns += staticfiles_urlpatterns()
