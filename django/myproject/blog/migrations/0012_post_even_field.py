# Generated by Django 2.1.7 on 2019-03-05 05:35

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190305_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='even_field',
            field=models.IntegerField(default=0, validators=[blog.models.Post.validation_even]),
            preserve_default=False,
        ),
    ]
