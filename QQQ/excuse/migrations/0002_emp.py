# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('excuse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('Empno', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('Ename', models.CharField(max_length=100)),
                ('Job', models.TextField(blank=True)),
                ('Mgr', models.PositiveIntegerField()),
                ('HireDate', models.DateTimeField()),
                ('Sal', models.FloatField()),
                ('Comm', models.PositiveIntegerField(null=True)),
                ('Deptno', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
