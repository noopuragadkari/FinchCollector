from django.shortcuts import render, redirect
import os
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Toy, Photo
from .forms import FeedingForm
import uuid
import boto3
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
  toys_finch_doesnt_have = Toy.objects.exclude(id__in = finch.toys.all().values_list('id'))
  return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': FeedingForm, 'toys' : toys_finch_doesnt_have })


def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

def assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('detail', finch_id=finch_id)

def add_photo(request, finch_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, finch_id=finch_id)
        except:
            print('An error occurred uploading file to S3')
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