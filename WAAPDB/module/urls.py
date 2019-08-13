from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('work', views.work),
    path('authorization', views.sign_in),
]