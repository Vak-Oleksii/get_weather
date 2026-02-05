from django.shortcuts import render
from .models import Cities, Weather
# Create your views here.
def database(request):
    database = Weather.objects.all()
    return render(request,'main/index.html', {'database':database})