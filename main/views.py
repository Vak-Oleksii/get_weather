from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    appid = '28a557698947871bf02a37766f0e0543'
    city = 'London'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}'

    response = requests.get(url)
    print(response.text)
    print(url)

    data = {
        'title': 'Головна сторінка',

    }
    return render(request,'main/index.html', data)

def about(request):
    return render(request,'main/about.html')
