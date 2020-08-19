from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from main_app.views import createviews, renderviews

urlpatterns = [
    # render urls

]
urlpatterns += staticfiles_urlpatterns()
