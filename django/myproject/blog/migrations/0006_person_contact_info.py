# Generated by Django 2.1.7 on 2019-03-05 03:47

import blog.models
from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_person_year_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='contact_info',
            field=jsonfield.fields.JSONField(default=blog.models.Person.contact_default, verbose_name='연락처'),
        ),
    ]
