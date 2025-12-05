from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

days_of_week = {
    'monday': 'Pienso, luego existo. ',
    'tuesday': 'La vida es un sueño. ',
    'wednesday': 'El tiempo es oro. ',
    'thursday': 'Se el cambio que quieres ver. ',
    'friday': 'Solo se que nada se. ',
    'saturday': 'El conocimiento es poder. ',
    'sunday': 'La vida es bella. '
}


def index(request):
    days = list(days_of_week.keys())  # [monday, tuesday, ...]
    return render(request, "quotes/index.html", {"days": days})


def days_week_with_number(request, day):
    days = list(days_of_week.keys())
    if day > len(days):
        return HttpResponseNotFound("El dia no existe o es invalido")
    redirect_day = days[day-1]
    redirect_path = reverse("day-quote", args=[redirect_day])
    return HttpResponseRedirect(redirect_path)


def days_week(request, day):
    try:
        quote_text = days_of_week[day]
        return HttpResponse(quote_text)
    except Exception:  # o KeyError
        return HttpResponseNotFound(f'{day}: No es valido <a href="#" onclick="history.back();">Regresar atrás</a>')
