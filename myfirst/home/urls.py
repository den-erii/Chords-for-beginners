from django.urls import path

from .views import *

urlpatterns = [
    path('', video, name='video'),
    path('about/', about, name='about'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('yoursong/', add_song, name='add_song'),
    path('songs/', songs_list, name='songs_list'),
    path('songs/<int:pk>', song, name='song'),
    # path('magic/', video, name='video'),
    path('main/', videos, name='videos'),
    path('search_results', SearchResultsView.as_view(), name='search_results'),
]
