# Generated by Django 3.2 on 2021-04-24 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=20)),
                ('description', models.TextField(blank=True, default='', max_length=200)),
                ('location', models.IntegerField(choices=[(1, 'Main'), (2, 'Archive'), (3, 'Trash')], default=1)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default='', max_length=200)),
                ('category', models.IntegerField(choices=[(1, 'Task'), (2, 'Feature'), (3, 'Bug'), (4, 'Other')], default=1)),
                ('priority', models.IntegerField(choices=[(1, 'None'), (2, 'Low'), (3, 'Medium'), (4, 'High')], default=1)),
                ('status', models.IntegerField(choices=[(1, 'Backlog'), (2, 'In Progess'), (3, 'Testing'), (4, 'Completed')], default=1)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(default=None, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='rest_api.project')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProjectMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_level', models.IntegerField(choices=[(1, 'Share'), (2, 'Edit'), (3, 'View')], default=3)),
                ('owner', models.ForeignKey(default=None, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='projectMemberships', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(default=None, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='projectMemberships', to='rest_api.project')),
            ],
            options={
                'ordering': ['id'],
                'unique_together': {('project', 'owner')},
            },
        ),
    ]
