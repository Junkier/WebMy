# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('excuse', '0002_emp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp2',
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
        migrations.RemoveField(
            model_name='emp',
            name='Deptno',
        ),
        migrations.RemoveField(
            model_name='emp',
            name='HireDate',
        ),
        migrations.RemoveField(
            model_name='emp',
            name='Mgr',
        ),
        migrations.AlterField(
            model_name='emp',
            name='Comm',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emp',
            name='Ename',
            field=models.TextField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emp',
            name='Job',
            field=models.TextField(max_length=10),
            preserve_default=True,
        ),
    ]
