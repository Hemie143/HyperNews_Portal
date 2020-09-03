from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request, *args, **kwargs):
        if request.POST.get('todo') not in self.all_todos:
            self.all_todos.append(request.POST.get('todo'))
        return redirect('/')
