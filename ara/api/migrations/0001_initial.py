#  Copyright (c) 2019 Red Hat, Inc.
#
#  This file is part of ARA Records Ansible.
#
#  ARA is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  ARA is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with ARA.  If not, see <http://www.gnu.org/licenses/>.

# Generated by Django 2.1.7 on 2019-03-19 00:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('path', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'files',
            },
        ),
        migrations.CreateModel(
            name='FileContent',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('sha1', models.CharField(max_length=40, unique=True)),
                ('contents', models.BinaryField(max_length=4294967295)),
            ],
            options={
                'db_table': 'file_contents',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('facts', models.BinaryField(max_length=4294967295)),
                ('alias', models.CharField(max_length=255, null=True)),
                ('changed', models.IntegerField(default=0)),
                ('failed', models.IntegerField(default=0)),
                ('ok', models.IntegerField(default=0)),
                ('skipped', models.IntegerField(default=0)),
                ('unreachable', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'hosts',
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.BinaryField(max_length=4294967295)),
            ],
            options={
                'db_table': 'labels',
            },
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('started', models.DateTimeField(default=django.utils.timezone.now)),
                ('ended', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('uuid', models.UUIDField()),
                ('status', models.CharField(choices=[('unknown', 'unknown'), ('running', 'running'), ('completed', 'completed')], default='unknown', max_length=25)),
            ],
            options={
                'db_table': 'plays',
            },
        ),
        migrations.CreateModel(
            name='Playbook',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('started', models.DateTimeField(default=django.utils.timezone.now)),
                ('ended', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('ansible_version', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('unknown', 'unknown'), ('running', 'running'), ('completed', 'completed'), ('failed', 'failed')], default='unknown', max_length=25)),
                ('arguments', models.BinaryField(max_length=4294967295)),
                ('path', models.CharField(max_length=255)),
                ('labels', models.ManyToManyField(to='api.Label')),
            ],
            options={
                'db_table': 'playbooks',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=255)),
                ('value', models.BinaryField(max_length=4294967295)),
                ('type', models.CharField(max_length=255)),
                ('playbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='api.Playbook')),
            ],
            options={
                'db_table': 'records',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('started', models.DateTimeField(default=django.utils.timezone.now)),
                ('ended', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('ok', 'ok'), ('failed', 'failed'), ('skipped', 'skipped'), ('unreachable', 'unreachable'), ('changed', 'changed'), ('ignored', 'ignored'), ('unknown', 'unknown')], default='unknown', max_length=25)),
                ('content', models.BinaryField(max_length=4294967295)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='api.Host')),
                ('play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='api.Play')),
                ('playbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='api.Playbook')),
            ],
            options={
                'db_table': 'results',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('started', models.DateTimeField(default=django.utils.timezone.now)),
                ('ended', models.DateTimeField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('action', models.TextField()),
                ('lineno', models.IntegerField()),
                ('tags', models.BinaryField(max_length=4294967295)),
                ('handler', models.BooleanField()),
                ('status', models.CharField(choices=[('unknown', 'unknown'), ('running', 'running'), ('completed', 'completed')], default='unknown', max_length=25)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.File')),
                ('play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.Play')),
                ('playbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.Playbook')),
            ],
            options={
                'db_table': 'tasks',
            },
        ),
        migrations.AddField(
            model_name='result',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='api.Task'),
        ),
        migrations.AddField(
            model_name='play',
            name='playbook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plays', to='api.Playbook'),
        ),
        migrations.AddField(
            model_name='host',
            name='playbook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to='api.Playbook'),
        ),
        migrations.AddField(
            model_name='file',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='api.FileContent'),
        ),
        migrations.AddField(
            model_name='file',
            name='playbook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='api.Playbook'),
        ),
        migrations.AlterUniqueTogether(
            name='record',
            unique_together={('key', 'playbook')},
        ),
        migrations.AlterUniqueTogether(
            name='host',
            unique_together={('name', 'playbook')},
        ),
        migrations.AlterUniqueTogether(
            name='file',
            unique_together={('path', 'playbook')},
        ),
    ]
