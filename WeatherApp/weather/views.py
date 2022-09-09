from django.shortcuts import render
import requests


def index(request):
    appid = 'ce74fb3a11b3efd69204863a42c50de9'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = 'Minsk'
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }
    context = {'info': city_info}

    return render(request, 'weather/index.html', context)
