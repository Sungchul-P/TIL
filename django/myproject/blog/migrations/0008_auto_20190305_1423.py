# Generated by Django 2.1.7 on 2019-03-05 05:23

import builtins
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190305_1417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': [builtins.id]},
        ),
    ]
