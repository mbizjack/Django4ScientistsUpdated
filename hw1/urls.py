from django.urls import path

from . import views

app_name = 'hw1'
urlpatterns = [
    path('', views.index, name='index'),
]