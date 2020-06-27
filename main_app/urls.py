from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from main_app.views import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('candidatecreate', views.candidatecreate, name='candidatecreate'),
    path('candidatelogin', views.candidatelogin, name='candidatelogin'),

]
urlpatterns += staticfiles_urlpatterns()
