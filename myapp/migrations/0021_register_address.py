# Generated by Django 5.1.6 on 2025-03-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_alter_register_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
