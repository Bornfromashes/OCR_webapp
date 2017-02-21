# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('Reg_no', models.IntegerField()),
            ],
            options={
                'db_table': 'Student_info',
            },
        ),
    ]
