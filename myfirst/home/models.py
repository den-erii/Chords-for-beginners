from django.db import models
from django.contrib.auth.models import User

class Friends(models.Model):
    objects = None
    username = models.TextField(blank=True)


class Song(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=u"Пользователь")
    author = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"Автор")
    song_name = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"название песни")
    lyrics = models.TextField(max_length=500, blank=True, null=True, verbose_name=u"Текст песни")
    song_link = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"Ссылка на песню(YouTube)")

    class Meta:
        app_label = 'home'
        ordering = ["-song_name"]

    def __str__(self):
        return self.author + ' - ' + self.song_name
