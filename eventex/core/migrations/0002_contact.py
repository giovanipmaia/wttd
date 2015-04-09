# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.CharField(max_length=1, verbose_name='tipo', choices=[(b'P', 'Telefone'), (b'E', 'E-mail'), (b'F', 'Fax')])),
                ('value', models.CharField(max_length=255, verbose_name='valor')),
                ('speaker', models.ForeignKey(verbose_name='palestrante', to='core.Speaker')),
            ],
        ),
    ]
