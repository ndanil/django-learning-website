from django.http import HttpResponse
from django.template import loader

from .models import News


def index(request):
    latest_question_list = News.objects.order_by('time')[:5]
    template = loader.get_template('news/news.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
