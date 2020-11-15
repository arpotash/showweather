import requests
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from mainapp.forms import CityForm
from mainapp.models import City


def main(request):
    api_key = ''
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='
    all_cities = []
    all_cities_revers = []
    if request.method == 'POST':
        city_form = CityForm(request.POST)
        if city_form.is_valid():
            check_city_form = city_form.cleaned_data['name']
            res = requests.get(url.format(check_city_form)).json()
            if res['cod'] == '404':
                raise KeyboardInterrupt
            else:
                city_form.save()

    city_form = CityForm()
    cities = City.objects.all()
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'name': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)
    all_cities_revers = list(reversed(all_cities))
    context = {
        'title': 'погода на сегодня',
        'cities': all_cities_revers[:5],
        'form': city_form
    }
    return render(request, 'mainapp/index.html', context)
