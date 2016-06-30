#afc Writing more views --> http://docs.djangoproject.com/en/1.9/intro/tutorial03/
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hola, esta es la página principal de la aplicación de encuestas.")

