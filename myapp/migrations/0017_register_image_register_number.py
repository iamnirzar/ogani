# Generated by Django 5.1.6 on 2025-03-04 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_rename_addtocart_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='image',
            field=models.ImageField(default=1, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='number',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
