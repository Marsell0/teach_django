from django import template
from books.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    return Category.objects.filter(pk=filter)


@register.inclusion_tag('books/list_cats.html', name='show_cats')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}


@register.simple_tag()
def get_posts(filter=None):
    if not filter:
        return Books.objects.all()
    return Books.objects.filter(pk=filter)


@register.inclusion_tag('books/show_posts.html')
def show_posts(cats_id=''):
    if cats_id == '':
        posts = Books.objects.all()
    else:
        posts = Books.objects.filter(cat_id=cats_id)
    return {'posts': posts}
