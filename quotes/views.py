from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

days_of_week={
    'monday':'Pienso, luego existo. ',
    'tuesday':'La vida es un sueño. ',
    'wednesday':'Eltiempo es oro. ',
    'thursday':'Se el cambio que quieres ver. ',
    'friday':'Solo se que nada se. ',
    'saturday':'El conocimiento es poder. ',
    'sunday': 'La vida es bella. '
}

def days_week_with_number(request,day):
    return HttpResponse(day)
    
def days_week(request, day):
    try:
        quote_text=days_of_week[day] 
        return HttpResponse(quote_text)
    except:
        return HttpResponseNotFound(f'{day}: No es valido ')

    # else:
    #     
