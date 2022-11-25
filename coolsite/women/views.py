from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *
# Create your views here.
menu=['о сайте', 'добавить статью','os', 'login']

def index(request):
    posts=Women.objects.all()
    return render(request, 'women/index.html',{'title':'title','menu':menu,'posts':posts})

def about(request):
    return render(request,'women/about.html', {'title':'about','menu':menu})

def categories(request, catid):
    return HttpResponse(f'cat: {catid}')

def pageNotFound(request,exception):
    return HttpResponseNotFound('Стр не найдена')