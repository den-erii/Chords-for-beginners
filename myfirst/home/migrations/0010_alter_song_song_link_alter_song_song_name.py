# Generated by Django 4.0.6 on 2022-07-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_delete_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_link',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='URL-адрес песни(YouTube)'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Название песни'),
        ),
    ]