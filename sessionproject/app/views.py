from django.shortcuts import render

# Create your views here.


def home(request):
    request.session['todos'] = []
    return render(request, 'index.html')


def save(request):
    todo = request.GET['todo']
    todos = request.session.get('todos', [])
    todos.append(todo)

    request.session['todos'] = todos
    return render(request, 'index.html')
