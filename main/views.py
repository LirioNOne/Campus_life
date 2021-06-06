from django.shortcuts import render

from .models import News


def index(request):
    news = News.objects.order_by('-id')
    return render(request, 'main/index.html',{
       # 'title': news_name здесь нужно сделать формочку
    })
