from django.shortcuts import render
from django.http import response, HttpResponse


def home(request):
    return HttpResponse("<h1>Holle Word</h1>")

