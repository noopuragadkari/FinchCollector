from django.shortcuts import render
from django.http import HttpResponse
from .models import Finch
import logging 
logging.basicConfig(level=logging.DEBUG)

from django.db import models

# Create your views here.
def home(request):
    """
    home view
    http://localhost:8000
    """
    return HttpResponse("hello world")

def about(request):
  """
   home view
    http://localhost:8000/about
  """
  return render(request, 'about.html')

def finches_index(request):
  """
   cats index page
    http://localhost:8000/finches
  """
  finches = Finch.objects.all()
  return render(request, 'finches/index.html',{'finches':finches})