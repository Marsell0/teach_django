from django.shortcuts import render, HttpResponse
from .models import *

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

# Create your views here.
def index(request):
    posts = Books.objects.all()
    return render(request, 'books/index.html', {'posts': posts, 'menu': menu})


def about(request):
    return render(request, 'books/about.html', {'menu': menu})


def categories(request, cat):
    return HttpResponse(f'<h1>Страница категорий</h1><p>{cat}</p>')