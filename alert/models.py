from django.db import models
from datetime import datetime

# Create your models here.
class AlertInfo(models.Model):
    TIME_FRAME_TYPE = (
        (1,'minutes'),
        (2,'hours'),
        (3,'days'),
    )

    info_id = models.CharField('id', max_length=20, primary_key=True)
    title = models.CharField('标题', max_length=30)
    message = models.TextField('信息内容')
    time_frame_type = models.CharField('检测时间段类型', choices=TIME_FRAME_TYPE, max_length=10)
    time_frame_num = models.IntegerField('检测时间段长度')
    update_time = models.DateTimeField('更新时间', auto_now=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '预警事件基本信息'
        verbose_name_plural = verbose_name


class AlertRule(models.Model):
    ALERT_TYPE = (
        (1,'minutes'),
        (2,'hours'),
    )

    rule_id = models.CharField('规则id', max_length=20, primary_key=True)
    info_id = models.ForeignKey(AlertInfo, verbose_name='预警事件基本信息', on_delete=models.CASCADE)
    alert_type = models.CharField('警告类型', choices=ALERT_TYPE, max_length=10)
    address = models.CharField('联系方式', max_length=50)
    numevents = models.IntegerField('更新时间')

    class Meta:
        verbose_name = '预警具体规则'
        verbose_name_plural = verbose_name


class AlertEvent(models.Model):

    event_id = models.CharField('事件id', max_length=20, primary_key=True)
    info_id = models.ForeignKey(AlertInfo, verbose_name='预警事件基本信息', on_delete=models.DO_NOTHING)
    time = models.DateTimeField('创建时间', default=datetime.now)

    class Meta:
        verbose_name = '预警事件'
        verbose_name_plural = verbose_name