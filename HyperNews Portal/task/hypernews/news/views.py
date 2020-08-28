from django.http import HttpResponse
from django.views import View
from django.conf import settings
from django.shortcuts import render

import json


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        html = "Coming soon"
        return HttpResponse(html)

class NewsView(View):
    def get(self, request, link_nr, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, 'r', encoding='utf-8') as news_file:
            news_from_json = json.load(news_file)
        news = [n for n in news_from_json if n['link'] == link_nr][0]
        print(news)
        context = {'created': news['created'], 'text': news['text'], 'title': news['title']}
        return render(request, 'news/news.html', context=context)
