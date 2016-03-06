# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command


class Migration(migrations.Migration):

    def load_data(apps, schema_editor):
        call_command('loaddata', 'user.json')

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]
