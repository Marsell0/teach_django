from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Страница Books')


def categories(request):
    return HttpResponse('<h1>Страница категорий</h1>')