from django.shortcuts import render
from news.models import Articles

def index(request):
    new = Articles.objects.order_by('-date')[:3]
    return render(request, 'menu/index.html', {'new': new})


def contact(request):
    return render(request, 'menu/contact.html', {'title': 'Контакты'})


def login(request):
    return render(request, 'user/login.html', {'title': 'Регистрация'})