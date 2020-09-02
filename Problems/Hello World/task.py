from django.http import HttpResponse
from django.views import View


class HelloWorldView(View):
    def get(self, request, *args, **kwargs):
        html = "Hello, World!"
        return HttpResponse(html)
