# Generated by Django 3.2 on 2021-05-27 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_auto_20210516_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
    ]
