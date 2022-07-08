from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views import View
from .forms import *
from django.db.models import Q




from home.utils import DataMixin, menu

def videos(request):
    return render(request, 'home/videos.html', {'title': 'Главная страница'})

#def home(request):
#    return render(request, 'home/base.html', {'title': 'Главная'})

def video(request):
    return render(request, 'home/video.html', {'title': 'Magic'})

def about(request):
    return render(request, 'home/about.html', {'title': 'О нас'})

def add_song(request):
     return render(request, 'home/add_song.html', {'title': 'Добавь свою музыку'})


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
        return redirect('videos')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'home/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('videos')

class LogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect("videos")

def add_song(request):
    if request.method == 'POST':
        form = song_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("videos")
    else:
        form = song_form()
    return render(request, "home/add_song.html", {'form': form, 'title': 'Добавь музыку'})

class SearchResultsView(ListView):
    model = Song
    template_name = 'home/search_results.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Song.objects.filter(
            Q(author__icontains=query) | Q(song_name__icontains=query)
        )
        return object_list

def songs_list(request):
    songs = Song.objects.all()
    paginator = Paginator(songs, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home/songs_list.html', {"songs": songs, "page_obj": page_obj})

def song(request, pk):
    song = Song.objects.get(pk=pk)
    lyrics = song.lyrics
    chords = ['A ', 'Am ', ' Am', 'A#', 'B ', 'Bm ', ' Bm', 'C ', 'Cm ', ' Cm', 'C#', 'D ', 'Dm ', ' Dm', 'D# ', 'E ', ' E ', ' E7 ', 'E7 ', 'Em ', ' Em', 'F ', ' F', 'Fm ', ' Fm', 'F# ', 'G ', ' G', 'Gm ', ' Gm', 'G# ']
    song_chords = set()
    for chord in chords:
        if chord in lyrics:
            song_chords.add(chord)
    song_chords = list(song_chords)
    for i in range(len(song_chords)):
        song_chords[i] = song_chords[i].replace(" ", "")
        song_chords[i] = song_chords[i].replace("#", "diez")
    song_chords = set(song_chords)

    if song.song_link is None:
        return render(request, 'home/song.html', {"song": song, "song_chords": song_chords})
    else:
        link = song.song_link
        a = link[:17]
        b = link[17:]
        link = "https://www.youtube.com/" + "embed/" + b
        return render(request, 'home/song.html', {"song": song, "link": link, "song_chords": song_chords, "a": a})


