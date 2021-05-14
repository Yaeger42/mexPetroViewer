from backend.mexpetrols.visualizationapp.views import display_resume
from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_resume)
]