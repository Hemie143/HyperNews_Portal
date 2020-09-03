from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request, *args, **kwargs):
        if request.POST.get('todo'):
            if request.POST.get('todo') not in self.all_todos:
                if request.POST.get('important'):
                    self.all_todos.insert(0, request.POST.get('todo'))
                else:
                    self.all_todos.append(request.POST.get('todo'))
        return redirect('/')
ep