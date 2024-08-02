from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import Todo

# Create your views here.
@login_required(login_url='login')
def home(request):
    todos = Todo.objects.all()
    return render(request, 'tasks_a/home.html', {'todos': todos})

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