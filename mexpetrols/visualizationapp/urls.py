from django.urls import path
from . import views 

urlpatterns = [
    path('vis/methane/', views.methane_derivatives),
    path('vis/gasoline/', views.gasoline_prices),
    path('vis/actives/', views.actives_prices)
]