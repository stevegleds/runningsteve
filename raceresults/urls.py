# Race Results url file
from django.urls import path
from runningsteve import views

urlpatterns = [
    path('', views.index, name='index'),
]
