# Generated by Django 3.1.14 on 2023-07-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='spotify_id',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='spotify_id',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
