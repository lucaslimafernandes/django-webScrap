from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from datetime import datetime

import csv


import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["PATH"] += os.pathsep + os.path.join(BASE_DIR,'/gecko')

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary



# Create your views here.

from . tests import busca_zoom

def index(request):
    if request.method == 'GET':
        return render(request, 'app/buscar.html')
    
    elif request.method == 'POST':
        
        busca = request.POST.get('busca')
        retorno = busca_zoom(busca)

        listaNome = []
        listaPreco = []
        for i in retorno['nome']:
            listaNome.append(i)
        for i in retorno['preco']:
            listaPreco.append(i)

        res = {}
        for i in range(0, len(listaNome)):
            res[i] = [listaNome[i], listaPreco[i]]    
            

        content = {'nomes': retorno['nome'], 'preco': retorno['preco']}

        #return HttpResponse(res)
        return render(request, 'app/resultados.html', {'retorno':res})
    
    else:
        return HttpResponse('ERRO INESPERADO, sistema em desenvolvimento!')



