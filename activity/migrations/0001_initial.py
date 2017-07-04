# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-04 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_id', models.PositiveIntegerField()),
                ('object_id', models.PositiveIntegerField()),
                ('target_id', models.PositiveIntegerField(blank=True, null=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('summary', models.CharField(blank=True, max_length=255)),
                ('actor_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities_actor', to='contenttypes.ContentType')),
                ('object_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='contenttypes.ContentType')),
                ('target_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activities_target', to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='verb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='activity.Verb'),
        ),
    ]