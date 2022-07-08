from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    author = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"Автор")
    song_name = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"Название песни")
    lyrics = models.TextField(max_length=500, blank=True, null=True, verbose_name=u"Текст песни")
    song_link = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"URL-адрес песни(YouTube)")


    class Meta:
        app_label = 'home'
        ordering = ["song_name"]

    def __str__(self):
        return self.author + ' - ' + self.song_name

