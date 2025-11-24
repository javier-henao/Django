from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hola mundo desde Django!")

def monday(request):
    return HttpResponse("Hola lunes!")

def tuesday(request):
    return HttpResponse("Hola martes!")

def wednesday(request):
    return HttpResponse("Hola miercoles!")