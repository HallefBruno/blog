from django.shortcuts import render
from django.http import response, HttpResponse


def home(request):
    return render(request, 'blog/home.html')
