from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('friends/', friends, name='friends'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_song', add_song, name='add_song'),
]
