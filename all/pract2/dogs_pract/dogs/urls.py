from django.urls import path
from . import views

urlpatterns = [
    path('', views.dog_breeds, name='dog_breeds'),
]