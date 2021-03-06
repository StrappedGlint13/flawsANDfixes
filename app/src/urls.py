from django.urls import path

from django.http import HttpResponse
from django.template import loader

from .models import Question

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('polls/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('polls/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('app/<int:question_id>/vote/', views.vote, name='vote'), 
]