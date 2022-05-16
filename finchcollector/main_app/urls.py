from django.urls import path
from .import views

urlpatterns = [
    #http://localhost:8000
    path('', views.home, name='home'),
    #http://localhost:8000/about/
    path('about/', views.about, name='about'),
     #http://localhost:8000/finches/
    path('finches/', views.finches_index, name='index'),

    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
]