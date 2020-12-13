from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=fe55faa7bf11571932bf0b2ba623f7df').read() 

        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
  
        # data for variable list_of_data 
        data = { 
            "country_code": str(list_of_data['sys']['country']),
            "city": str(list_of_data['name']), 
            "weather": str(list_of_data['clouds']['all']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + ' °C', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
            "temp_min": str(list_of_data['main']['temp_min']) + ' °C', 
            "temp_max": str(list_of_data['main']['temp_max']) + ' °C', 
            "feels_like": str(list_of_data['main']['feels_like']) + ' °C', 
        } 
        print(data)
        
    else:
        data = {}
    return render(request, 'main/index.html', data)

