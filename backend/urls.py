# DjangoVueConnection/backend/urls.py

""" urls for the backend app """

from django.urls import path
from backend.views import DogsView


urlpatterns = [
   path('dogs/', DogsView.as_view(), name='dogs'),
]
