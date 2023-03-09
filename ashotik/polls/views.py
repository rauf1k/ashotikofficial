from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Добрий день, поставте залік будь-ласка по даному предмету, я не хочу на перездачу.")