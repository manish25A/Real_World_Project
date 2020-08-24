from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from main_app.views import createviews, renderviews

urlpatterns = [
    # render urls
    path('', renderviews.index, name='index'),
    path('login', renderviews.login, name='login'),
    path('about', renderviews.about, name='about'),
    path('candidatelogin', renderviews.candidatelogin, name='candidatelogin'),
    path('contactpage', renderviews.contactpage, name='contactpage'),
    path('aboutus', renderviews.aboutus, name='aboutus'),
    path("404", renderviews.page_not_found, name='404'),
    path("professional", renderviews.professional, name='professional'),
    path('dashboard', renderviews.dashboard, name='dashboard'),
    path('admindash', renderviews.AdminDashboard, name='admindash'),
    path('createadmin', renderviews.CreateAdmin, name='createadmin'),
    path('viewadmin', renderviews.ViewAdmin, name='viewadmin'),
    path('updateadmin', renderviews.UpdateAdmin, name='updateadmin'),
    path('deleteadmin', renderviews.DeleteAdmin, name='deleteadmin'),
    path('customerdash', renderviews.CustomerDashboard, name='customerdash'),
    path('createcustomer', renderviews.CreateCustomer, name='createcustomer'),
    path('viewcustomer', renderviews.ViewCustomer, name='viewcustomer'),
    path('updatecustomer', renderviews.UpdateCustomer, name='updatecustomer'),
    path('deletecustomer', renderviews.DeleteCustomer, name='deletecustomer'),
    path('jobspage', renderviews.jobspage, name='jobspage'),
    path('jobpost', renderviews.jobpost, name='jobpost'),

    # create urls
    path('contactsave', createviews.contactform, name='contactsave'),
    path('candidatecreate', createviews.candidatecreate, name='candidatecreate'),

]
urlpatterns += staticfiles_urlpatterns()
