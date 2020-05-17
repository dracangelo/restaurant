from . import views
from django.urls import path, include

app_name='reservation'

urlpatterns = [
    path('', views.reserve_table, name='reserve_table')
]