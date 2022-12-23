from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print('index')
    return render(request, 'events/start.html')
