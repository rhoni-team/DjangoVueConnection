# DjangoVueConnection/backend/views.py

""" Views for the backend app """

from django.views import View
from django.http import JsonResponse
from backend.models import Dog


class DogsView(View):
   """
   API endpoint for dogs data
   """
   def get(self, request):
       """
       Get all dogs data
       """
       dogs = Dog.objects.all().values()
       return JsonResponse(
           {'results': list(dogs)},
           status=200
       )
