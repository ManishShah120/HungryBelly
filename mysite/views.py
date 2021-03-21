from django.shortcuts import render
import folium

def home(request):
    return render(request, 'mysite/base.html')
