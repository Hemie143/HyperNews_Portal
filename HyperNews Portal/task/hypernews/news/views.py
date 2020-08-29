from django.http import HttpResponse
from django.views import View
from django.conf import settings
from django.shortcuts import render

import json
import datetime

class MainPageView(View):
    def get(self, request, *args, **kwargs):
        html = 'Coming soon'
        return HttpResponse(html)


class NewsAllView(View):
    def get(self, request, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, 'r', encoding='utf-8') as news_file:
            news_from_json = json.load(news_file)
        print(news_from_json)
        news = {}
        dates = sorted(set([n['created'][:10] for n in news_from_json]), reverse=True)
        for d in dates:
            news[d] = []
        for n in sorted(news_from_json, key=lambda item: item['created'], reverse=True):
            d = n['created'][:10]
            news[d].append(dict(link=n['link'], title=n['title']))
        return render(request, 'news/main.html', dict(newslist=news))


class NewsView(View):
    def get(self, request, link_nr, *args, **kwargs):
        with open(settings.NEWS_JSON_PATH, 'r', encoding='utf-8') as news_file:
            news_from_json = json.load(news_file)
        news = [n for n in news_from_json if n['link'] == link_nr][0]
        context = {'created': news['created'], 'text': news['text'], 'title': news['title']}
        return render(request, 'news/news.html', context=context)
