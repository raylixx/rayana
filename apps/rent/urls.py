
from django.contrib import admin
from django.urls import path, include

from apps.rent import views

urlpatterns = [
    path('', view=views.home, name='index.html'),
]

