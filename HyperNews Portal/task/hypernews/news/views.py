from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

class NewsView(View):
    def get(self, request, *args, **kwargs):
        html = "Coming soon"
        return HttpResponse(html)