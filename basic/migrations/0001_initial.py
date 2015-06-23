# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('solution', models.CharField(max_length=10, choices=[(b'a', b'A'), (b'b', b'B'), (b'c', b'C'), (b'd', b'D')])),
            ],
        ),
        migrations.CreateModel(
            name='Multiple_choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Single_choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=500)),
                ('solution', models.CharField(default=b'A', max_length=10, choices=[(b'a', b'A'), (b'b', b'B'), (b'c', b'C'), (b'd', b'D')])),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_name', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('duration', models.DecimalField(max_digits=5, decimal_places=0)),
                ('syllabus', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='single_choice',
            name='test_id',
            field=models.ForeignKey(to='basic.Test'),
        ),
        migrations.AddField(
            model_name='multiple_choice',
            name='test_id',
            field=models.ForeignKey(to='basic.Test'),
        ),
        migrations.AddField(
            model_name='choice',
            name='test_id',
            field=models.ForeignKey(to='basic.Multiple_choice'),
        ),
    ]
