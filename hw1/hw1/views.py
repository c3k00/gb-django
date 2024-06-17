from django.shortcuts import render
from django.http import HttpResponse
import logging

# Настройка логирования
logger = logging.getLogger(__name__)

def index(request):
    context = {
        "title": "Главная страница",
        "content": "Приветствую на главной странцие",
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        "title": "О себе",
    }
    return render(request, 'about.html', context)