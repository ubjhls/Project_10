from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404
from .models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model

# Create your views here.

def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request,'accounts/index.html',context)

def signup(request):
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, user_pk):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)
    context = {
        'user_profile' : user
    }
    return render(request,'accounts/detail.html', context)
