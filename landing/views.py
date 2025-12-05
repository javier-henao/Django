from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

# Create your views here.


def home(request):
    today = date.today()
    stack = [
        {
            'id': 'python',
            'name': 'Python'
        },
        {
            'id': 'django',
            'name': 'Django'
        },
        {
            'id': 'golang',
            'name': 'Golang'
        },
        {
            'id': 'js',
            'name': 'JS'
        },
    ]
    # stack = [] #
    return render(request, 'landing/landing.html', {
        "name": "Daniel",
        "today": today,
        "age": 12,
        "stack": stack,
    })


def stack_detail(request, tool):
    return HttpResponse(f"Tecnologia: {tool}")
