# Generated by Django 3.0.5 on 2020-04-19 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arizona', '0004_auto_20200406_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, unique=True),
        ),
    ]
