from . import views
from django.urls import path, include

app_name='aboutus'

urlpatterns = [
    path('', views.aboutus_list, name='aboutus_list')
]