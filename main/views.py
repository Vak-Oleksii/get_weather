from django.shortcuts import render
import requests
#from GetWeather.database.models import Cities
from .forms import CitiesForm
from .models import Cities


# Create your views here.
def index(request):

    appid = '28a557698947871bf02a37766f0e0543'

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid

    if request.method == 'POST':
        form = CitiesForm(request.POST)
        form.save()

    form = CitiesForm()

    all_cities = []
    cities = Cities.objects.all()
    for city in cities:
        response = requests.get(url.format(city.name)).json()
        data_info = {
            'city': city.name,
            'temp': response['main']['temp'],
            'icon': response['weather'][0]['icon'],

        }
        all_cities.append(data_info)


    for city in all_cities:
        print(city)
    print(url)
    context = {'data': all_cities, 'form': form,}


    return render(request,'main/index.html', context )

def about(request):
    return render(request,'main/about.html')
