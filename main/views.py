import requests

from django.shortcuts import render


def index(request):
    test = 'tets'
    return render(request, 'index.html')

