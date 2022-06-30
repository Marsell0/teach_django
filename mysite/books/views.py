from django.http import Http404
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *

menu = [
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]


def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница',
    }
    return render(request, 'books/index.html', context=context)


def about(request):
    return render(request, 'books/about.html', {'menu': menu})


def addpage(request):
    return HttpResponse('Добавить статью')


def show_post(request, post_id):
    post = get_object_or_404(Books, pk=post_id)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'books/post.html', context=context)


def contact(request):
    return HttpResponse('Контакты')


def login(request):
    return HttpResponse('Логин')


def categories(request, cat_id):
    context = {
        'menu': menu,
        'cat_selected': cat_id,
        'title': 'Отображение по категориям'
    }
    return render(request, 'books/index.html', context=context)