from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import News, Menu


def index(request):
    menuitems = Menu.objects.all();
    menus = []
    for menu in menuitems:
        lst = menu.menu_set.all()
        tmp = {}
        tmp['menu'] = menu
        tmp['sub'] = None
        if len(lst) > 0:
            tmp['sub'] = lst
        menus.append(tmp)
    context = {
        'menus': menus,
    }
    return render(request, 'news/index.html', context)


def singleNews(request, news_id):
    news2 = get_object_or_404(News, pk=news_id)
    context = {
        'news':news2
    }
    return render(request, 'news/singleNews.html', context)

def news(request):
    latest_question_list = News.objects.all().order_by('time')[:5]
    context = {
        'news':latest_question_list
    }
    return render(request, 'news/news.html', context)