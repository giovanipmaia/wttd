# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('url', models.URLField(verbose_name='Url')),
                ('description', models.TextField(verbose_name='Descri\xe7\xe3o', blank=True)),
            ],
        ),
    ]
