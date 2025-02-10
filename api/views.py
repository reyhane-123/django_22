from django.shortcuts import render
from django.http import HttpResponse
import string
import random
import requests
from django.http import JsonResponse

# Create your views here.
def generate_password(r):
    l=8
    ch=string.ascii_letters + string.digits
    p=''.join(random.choice(ch) for i in range(l))
    return HttpResponse(p)

def random_number(request):
    number=random.randint(1,1000)
    url=f"https://numbersapi.com/{number}"
    r=requests.get(url)
    f=r.text
    return render(requests , 'number/number.html' , {'number':random_number , 'fact': f})
 

def weather_info(request):
    r=requests.get('https://wttr.in/kerman?format=j1')
    data=r.json()['current_condition'][0]
    context={'temp_C': data['temp_C'],
           'windspeed_kmph': data['windspeedKmph'],
           'humidity': data['humidity'],
    }
    return render (r,data,context)

           



