from . import views
from django.urls import path, include

app_name='blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>', views.post_detail, name='post_detail'),
    path('category=<slug:category>', views.post_by_category, name='post_by_category'),
    path('tags=<slug:tag>', views.post_by_tag, name='post_by_tag'),
]