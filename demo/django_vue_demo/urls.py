"""urls for django_vue_demo project"""
from django.contrib import admin
from django.urls import path, re_path # add import re_path
from index_view.views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^.*', IndexView.as_view()), #add this line
]
