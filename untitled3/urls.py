"""untitled3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import django
from django.conf.urls import url
from django.contrib import admin

import news.views
from untitled3 import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', news.views.index, name='home'),
    url(r'^news/(?P<news_id>[0-9]+)/$', news.views.singleNews, name='singleNews'),
    url(r'^index',news.views.index),
    url(r'^news.html$', news.views.news, name='news'),
    url(r'^media/(?P<path>.*)$',django.views.static.serve,{'document_root' : settings.MEDIA_ROOT}),

]
