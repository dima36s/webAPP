from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1><b>Hello world!</b></h1>")


def about(request):
    return HttpResponse("<h1>Страница про нас</h1>")
