# Generated by Django 3.1 on 2023-04-16 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('naghd', 'پرداخت نقدی'), ('online', 'پرداخت آنلاین')], default='online', max_length=20, verbose_name='نحوه پرداخت'),
        ),
    ]
