# Generated by Django 4.0.6 on 2022-07-05 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_link',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Ссылка на песню(YouTube)'),
        ),
    ]
