from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from main_app.views.seeker import EditProfileView
from .views import *

# defining urls with appname and  name  than url

app_name = "accounts"

urlpatterns = [
    path('employee/register', RegisterEmployeeView.as_view(), name='employee-register'),
    path('employer/register', RegisterEmployerView.as_view(), name='employer-register'),
    path('employee/profile/update', EditProfileView.as_view(), name='employer-profile-update'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(), name='login'),
]
