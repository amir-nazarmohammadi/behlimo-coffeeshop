# Generated by Django 3.1 on 2023-04-16 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='نام میز')),
                ('is_reserved', models.BooleanField(default=False, verbose_name='رزرو شده است')),
            ],
            options={
                'verbose_name': 'میز',
                'verbose_name_plural': 'میزها',
            },
        ),
    ]
