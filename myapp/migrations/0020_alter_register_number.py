# Generated by Django 5.1.6 on 2025-03-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_alter_cart_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='number',
            field=models.IntegerField(default=1, max_length=15),
        ),
    ]
