# Generated by Django 5.1.6 on 2025-02-19 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_color_hexcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='hexcode',
        ),
    ]
