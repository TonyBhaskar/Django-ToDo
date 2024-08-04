from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import SignUpForm,TaskCreateForm
from django.contrib.auth.decorators import login_required
from .models import Todo

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
@login_required(login_url='login')
def home(request):
    todos = Todo.objects.all()
    paginator = Paginator(todos, 5)

    page = request.GET.get('page')

    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    context = {
        'todos': objects,
    }
    return render(request, 'tasks_a/test.html', context=context)

class LoginInterfaceView(LoginView):
    template_name = 'tasks_a/login_form.html'
    success_url = '/'

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'tasks_a/signup_form.html'
    success_url = '/'

def logout_view(request):
    logout(request)
    return redirect('login')

class TaskDeleteView(DeleteView):
    model = Todo
    template_name = 'tasks_a/task_confirm_delete.html'
    success_url = '/'

class TaskUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'completed']
    template_name = 'tasks_a/task_form.html'
    success_url = '/'

class TaskCreateView(CreateView):
    model = Todo
    form_class = TaskCreateForm
    template_name = 'tasks_a/task_create_form.html'
    success_url = '/'