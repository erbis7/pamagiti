from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *
# Create your views here.
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

def index(request):
    posts=Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }

    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request,'women/about.html', {'title':'about','menu':menu})

def categories(request, catid):
    return HttpResponse(f'cat: {catid}')

def pageNotFound(request,exception):
    return HttpResponseNotFound('Стр не найдена')

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")
def show_post(request, post_id):
    return HttpResponse(f"Отображение стр {post_id}")
