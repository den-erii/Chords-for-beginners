# Generated by Django 4.0.4 on 2022-07-07 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_song_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Friends',
        ),
    ]
