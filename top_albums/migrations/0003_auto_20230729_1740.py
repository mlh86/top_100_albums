# Generated by Django 3.1.14 on 2023-07-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_albums', '0002_auto_20230729_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='duration',
            field=models.DurationField(),
        ),
    ]
