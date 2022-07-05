from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

# from home.templates.home.forms import RegisterUserForm
from home.forms import RegisterUserForm, LoginUserForm
from home.models import Friends
from home.utils import DataMixin, menu


def index(request):
    return render(request, 'home/index.html', {'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return HttpResponse('Обратная связь')


# def login(request):
#     return HttpResponse('Авторизация')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Упс, ваша страница не найдена<h1>')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'home/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'home/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def friends(request):
    frds = Friends.objects.all()
    return render(request, 'home/friends.html', locals())
