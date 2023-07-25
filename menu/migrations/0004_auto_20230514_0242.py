# Generated by Django 3.1 on 2023-05-13 23:12

from django.db import migrations, models
import menu.models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20230411_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='gallery1',
            field=models.ImageField(blank=True, null=True, upload_to='menu/', validators=[menu.models.validate_image_size], verbose_name='گالری 1'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='gallery2',
            field=models.ImageField(blank=True, null=True, upload_to='menu/', validators=[menu.models.validate_image_size], verbose_name='گالری 2'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='gallery3',
            field=models.ImageField(blank=True, null=True, upload_to='menu/', validators=[menu.models.validate_image_size], verbose_name='گالری 3'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='menu/', validators=[menu.models.validate_image_size], verbose_name='تصویر آیتم'),
        ),
    ]
