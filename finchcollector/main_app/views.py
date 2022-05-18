from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
from .forms import FeedingForm
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

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': FeedingForm })


def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  success_url = '/finches/'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['description', 'lifespan']
  success_url = '/finches/'


class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'