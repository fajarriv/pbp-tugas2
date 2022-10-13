from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse,HttpRequest
from django.core import serializers
from todolist.forms import TaskForm


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')

    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user).all()
    context = {
        'task_list' : data_task,
    }
    return render(request, "todolist.html",context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = Task (
                user = request.user,
                title = form.cleaned_data["title"],
                description = form.cleaned_data["description"],
                date = datetime.date.today()
            )
            new_task.save()
            return redirect("todolist:show_todolist")
    
    form =TaskForm()
    context = {"form" : form}
    return render(request, "create_task.html", context)

@login_required(login_url='/todolist/login/')
def update_task(request,id):
    task = Task.objects.filter(pk=id)[0]
    if task.is_finished == True :
        task.is_finished = False
        task.save()
    else:
        task.is_finished = True
        task.save()
    return redirect("todolist:show_todolist")

@login_required(login_url='/todolist/login/')
def delete_task(request,id):
    task = Task.objects.filter(pk=id)[0]
    task.delete()
    return redirect("todolist:show_todolist")

@login_required(login_url='/todolist/login/')
def show_json(request):
    data_task = Task.objects.filter(user=request.user).all()
    return HttpResponse(serializers.serialize("json", data_task), content_type="application/json")

@login_required(login_url="/todolist/login")
def add_task(request):
    print(request.method)
    if request.method == "POST":
        task = Task(
            user=request.user,
            date=datetime.date.today(),
            title=request.POST["title"],
            description=request.POST["description"],
        )
        task.save()
        return HttpResponse(serializers.serialize("json", task), content_type="application/json")

    return HttpResponse("Invalid", status_code=405)