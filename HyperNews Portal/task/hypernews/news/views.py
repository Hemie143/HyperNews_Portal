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

class NewsCreate(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'news/create_form.html')

    def post(self, request, *args, **kwargs):
        # news_json_path = os.path.join(settings.BASE_DIR, '../', settings.NEWS_JSON_PATH)
        news_json_path = settings.NEWS_JSON_PATH
        with open(news_json_path, 'r') as news_json_file:
            news_feed = json.load(news_json_file)
            last_link = max([item['link'] for item in news_feed])
        with open(news_json_path, 'w') as news_json_file:
            news_item = {
                'created': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'text': request.POST.get('text'),
                'title': request.POST.get('title'),
                'link': last_link + 1
            }
            news_feed.append(news_item)
            json.dump(news_feed, news_json_file)
        return redirect('/news/')

