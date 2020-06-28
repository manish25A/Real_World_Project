from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from main_app.views import createviews, renderviews

urlpatterns = [
    #render urls
    path('', renderviews.index, name='index'),
    path('?=login', renderviews.login, name='login'),
    path('?=about', renderviews.about, name='about'),
    path('candidatelogin', renderviews.candidatelogin, name='candidatelogin'),
    path('?=contactpage', renderviews.contactpage, name='contactpage'),
    path('?=aboutus', renderviews.aboutus, name='aboutus'),


    #create urls
     path('contactsave', createviews.contactform, name='contactsave'),
     path('candidatecreate', createviews.candidatecreate, name='candidatecreate'),

]
urlpatterns += staticfiles_urlpatterns()
