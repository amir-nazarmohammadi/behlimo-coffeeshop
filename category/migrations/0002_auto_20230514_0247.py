# Generated by Django 3.1 on 2023-05-13 23:17

import category.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='media/', validators=[category.models.validate_image_size], verbose_name='تصویر دسته بندی'),
        ),
    ]
