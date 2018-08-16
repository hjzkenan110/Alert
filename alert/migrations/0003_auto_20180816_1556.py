# Generated by Django 2.0.2 on 2018-08-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0002_auto_20180815_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertrule',
            name='alert_type',
            field=models.CharField(choices=[(1, 'email'), (2, 'phone')], max_length=10, verbose_name='警告类型'),
        ),
    ]
