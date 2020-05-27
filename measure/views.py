# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import requests
# Create your views here.
def measure(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        latitude = request.GET['latitude']
        longitude = request.GET['longitude']
        terrainType = request.GET['terrainType']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'ph', 'value': value, 'latitude':latitude,'longitude':longitude, 'terrainType':terrainType}
            response = requests.post('http://pi1-eafit-fsosap.azurewebsites.net/temperatures/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://pi1-eafit-fsosap.azurewebsites.net/temperatures/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/measure.html", {'measures': measures})