# Generated by Django 4.0.6 on 2022-07-05 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_song'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['-song_name']},
        ),
    ]
