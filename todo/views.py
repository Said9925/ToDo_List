from django.shortcuts import render, redirect, HttpResponseRedirect
from todo.models import Todo


def index(request):
    posts = Todo.objects.all().order_by('id').values()
    return render(request, 'index.html', {"posts":posts})


def create(request):
    if request.POST:
        post = request.POST.get("title")
        posts = Todo(title=post)
        posts.save()
        return redirect("/")
    return render(request, 'create.html')


def edit(request, pk):
    posts = Todo.objects.get(pk=pk)

    if request.POST:
        posts.title = request.POST.get("title")
        posts.save()
        return redirect("/")

    return render(request, 'edit.html')



def delet(request, pk):
    posts = Todo.objects.get(pk=pk)
    posts.delete()
    return redirect("/")

