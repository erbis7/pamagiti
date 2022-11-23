from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('Out')
def categories(request, catid):
    return HttpResponse(f'cat: {catid}')

def pageNotFound(request,exception):
    return HttpResponseNotFound('Стр не найдена')