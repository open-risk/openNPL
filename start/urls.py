from django.urls import re_path
from . import views

app_name = 'start'

urlpatterns = [
    re_path(r'^$', views.Front.as_view(), name='Front'),
]