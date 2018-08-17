import json

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
from rest_framework import serializers
from rest_framework.views import APIView
import json
from . import models


class AlertInfoSerializer(serializers.Serializer):
    #AlertInfo表里面的字段序列化
    info_id = serializers.CharField()
    title = serializers.CharField()
    message = serializers.CharField()
    time_frame_type = serializers.ChoiceField(
        choices=[1, 2, 3],
        style={'minutes', 'hours', 'days'}
    )
    time_frame_num = serializers.IntegerField()
    update_time = serializers.DateTimeField()
    create_time = serializers.DateTimeField()


class AlertRuleSerializer(serializers.Serializer):
    alert_type = serializers.ChoiceField(
        choices=[1, 2],
        style={'email', 'phone'}
    )
    address = serializers.CharField()
    numevents = serializers.IntegerField()


class AlertInfo(APIView):

    def get(self,request,*args,**kwargs):
        # （Queryset）
        info = models.AlertInfo.objects.all()
        # 序列化，两个参数，instance:接受Queryset（或者对象）   
        # many=True表示对Queryset进行处理，manY=False表示对对象进行进行处理
        ser = AlertInfoSerializer(instance=info, many=True)
        # 转成json格式，ensure_ascii=False表示显示中文，默认为True
        info_data_list = ser.data

        for info in info_data_list:
            rule = models.AlertRule.objects.filter(info_id=info['info_id'])
            ser = AlertRuleSerializer(instance=rule, many=True)
            type(ser.data)
            info['alert']=ser.data
            # rule = json.dumps(ser.data, ensure_ascii=False)

        ret = json.dumps(info_data_list, ensure_ascii=False)
        return HttpResponse(ret)

    def post(self,request,*args,**kwargs):
        req = json.loads(request.body)
        return JsonResponse(data={})