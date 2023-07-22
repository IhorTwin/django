from django.http import HttpResponse

from django.shortcuts import render

import datetime


def index(request):
    return render(request, 'hiphop/index.html')


def greet(request, name):
    return render(request, 'hiphop/artist.html', {
        "name": name,
        "date": datetime.datetime.now(),
    })