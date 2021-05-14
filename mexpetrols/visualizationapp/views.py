from typing import List
from django.shortcuts import render
from .models import Gasolineprices, Methanepetrochemicals, Actives, Activecode
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.shortcuts import render
# Create your views here.

async def display_resume(request):
    display_model = Activecode.objects.all()
    return render(request, 'visualizationapp/index.html', {'activeCode': display_model})

