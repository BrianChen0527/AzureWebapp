from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate', views.calc, name='calculate'),
    path('hist_log', views.hist_log, name='hist_log'),
]