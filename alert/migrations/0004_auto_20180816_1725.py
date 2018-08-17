# Generated by Django 2.0.2 on 2018-08-16 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0003_auto_20180816_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertinfo',
            name='time_frame_type',
            field=models.CharField(choices=[('minutes', 'minutes'), ('hours', 'hours'), ('days', 'days')], max_length=10, verbose_name='检测时间段类型'),
        ),
        migrations.AlterField(
            model_name='alertrule',
            name='alert_type',
            field=models.CharField(choices=[('email', 'email'), ('phone', 'phone')], max_length=10, verbose_name='警告类型'),
        ),
    ]