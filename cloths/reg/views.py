<<<<<<< HEAD
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.urls import reverse_lazy

from reg.forms import LoginUserForm
from store.models import ClothsData


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегались')
            return redirect('login_url')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserCreationForm()
    return render(request, 'reg/register.html', {'form': form})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'reg/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

    def get_user_context(self, **kwargs):
        context = kwargs
        return context


def logout_user(request):
    logout(request)
    return redirect('login_url')

def new_func(request):
    return HttpResponse("Some new http page")
=======
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.urls import reverse_lazy

from reg.forms import LoginUserForm
from store.models import ClothsData


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегались')
            return redirect('login_url')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserCreationForm()
    return render(request, 'reg/register.html', {'form': form})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'reg/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

    def get_user_context(self, **kwargs):
        context = kwargs
        return context


def logout_user(request):
    logout(request)
    return redirect('login_url')


def new_func(request):
    return HttpResponse("Some new http page")
>>>>>>> branch_one
