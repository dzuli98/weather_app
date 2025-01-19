from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=81c1380840aca3564e06d3ccb0666897').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure'])
        }
    else:
        city=''
        data = {}
    return render(request, 'index.html', {'city':city, 'data': data })
