from django.shortcuts import render
from django.http import HttpResponse
import logging 
logging.basicConfig(level=logging.DEBUG)

from django.db import models


class Finch: 
  def __init__(self, name, description, lifespan):
    self.name = name
    self.description = description
    self.lifespan = lifespan

finches = [
  Finch('The Spice Finch', 'Is a sparrow-sized estrildid finch native to tropical Asia', 3),
  Finch('The Zebra Finch', 'The Australian zebra finch or chestnut-eared finch is the most common estrildid finch of Central Australia.', 2),
  Finch('The Strawberry Finch',' It is found in the open fields and grasslands of tropical Asia and is popular as a cage bird due to the colourful plumage of the males in their breeding season.', 3),
  Finch('Double-Barred Finch', 'The double-barred finch is an estrildid finch found in dry savannah.', 2)
]

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
  return render(request, 'finches/index.html',{'finches':finches})