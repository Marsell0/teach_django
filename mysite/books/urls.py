from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<slug:cat>/', categories, name='categories'),
    path('about/', about, name='about'),
]