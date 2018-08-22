import json
from datetime import datetime, timedelta

from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt 
from django.core.mail import send_mail
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
from rest_framework import serializers
from rest_framework.views import APIView

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
    
    def delete(self, request, info_id,  *args,**kwargs):
        # 批量删除(/1,2,3/)，用info_id逗号分隔开
        if ',' in info_id:
            info_id_list = info_id.strip(',').split(',')
            for per_id in info_id_list:
                result = models.AlertInfo.objects.filter(info_id=int(per_id)).delete()
            
            return JsonResponse({"msg": "Success!"})

        else:
            result = models.AlertInfo.objects.filter(info_id=info_id).delete()
            return JsonResponse({"msg": "Success!"})


    def get(self, request, info_id, *args,**kwargs):
        info = models.AlertInfo.objects.filter(info_id=info_id)
        # 序列化，两个参数，instance:接受Queryset（或者对象）   
        # many=True表示对Queryset进行处理，manY=False表示对对象进行进行处理
        ser = AlertInfoSerializer(instance=info, many=True)
        try:
            info_data = ser.data[0]
        except:
            ret = json.dumps({"msg": "Id does not exitst"}, ensure_ascii=False)
            return HttpResponse(ret)

        rule = models.AlertRule.objects.filter(info_id=info_data['info_id'])
        ser = AlertRuleSerializer(instance=rule, many=True)
        info_data['alert']=ser.data
        # rule = json.dumps(ser.data, ensure_ascii=False)

        ret = json.dumps(info_data, ensure_ascii=False)
        return HttpResponse(ret)
    
    def put(self, request, info_id, *args,**kwargs):
        info_id = int(info_id)

        req = json.loads(request.body)

        info = models.AlertInfo.objects.get(info_id=info_id)
        info.title = req['title']
        info.message = req['message']
        info.time_frame_type=req['time_frame_type']
        info.time_frame_num=req['time_frame_num']
        info.save()

        # 删除之前相关的规则
        models.AlertRule.objects.filter(info_id=info).delete()

        for alert_info in req['alert']:
            ar = models.AlertRule.objects.create(
                info_id=info, 
                alert_type=alert_info['alert_type'], 
                address=alert_info['address'], 
                numevents=int(alert_info['numevents'])
            )
        return JsonResponse({"msg": "Success!"})


class StartInfo(APIView):
    def get(self, request, *args,**kwargs):
        info = models.AlertInfo.objects.all()
        ser = AlertInfoSerializer(instance=info, many=True)
        info_data_list = ser.data

        for info in info_data_list:
            rule = models.AlertRule.objects.filter(info_id=info['info_id'])
            ser = AlertRuleSerializer(instance=rule, many=True)
            info['alert']=ser.data

        ret = json.dumps(info_data_list, ensure_ascii=False)
        return HttpResponse(ret)
    
    def post(self,request,*args,**kwargs):
        req = json.loads(request.body)
        ai = models.AlertInfo.objects.create(
            title=req['title'], 
            message=req['message'], 
            time_frame_type=req['time_frame_type'], 
            time_frame_num=req['time_frame_num']
        )
        for alert_info in req['alert']:
            ar = models.AlertRule.objects.create(
                info_id=ai, 
                alert_type=alert_info['alert_type'], 
                address=alert_info['address'], 
                numevents=int(alert_info['numevents'])
            )
        return JsonResponse({"id": ai.info_id})


class UpdateInfo(APIView):
    def get(self, request, info_id, *args,**kwargs):
        info = models.AlertInfo.objects.filter(info_id=info_id)
        ser = AlertInfoSerializer(instance=info, many=True)
        try:
            info_data = ser.data[0]
        except:
            ret = json.dumps({"msg": "Id does not exitst"}, ensure_ascii=False)
            return HttpResponse(ret)

        rule = models.AlertRule.objects.filter(info_id=info_data['info_id'])
        ser = AlertRuleSerializer(instance=rule, many=True)

        tmp = json.dumps(ser.data)
        info_data['alert'] = json.loads(tmp)
        # 取出转义字符
        
        print(json.dumps(info_data, ensure_ascii=False))
        return render(request, "edit.html", info_data)


# 警报事件
class AlertEvent(APIView):
    def post(self, request, info_id, *args,**kwargs):
        try:
            info = models.AlertInfo.objects.get(info_id=info_id)
        except:
            return JsonResponse({"msg": "Id does not exitst"})

        event = models.AlertEvent.objects.create(info_id=info)
        rules = models.AlertRule.objects.filter(info_id=info)

        date_end = datetime.now()
        if info.time_frame_type == 'days':
            timespan = timedelta(days=info.time_frame_num)
        elif info.time_frame_type == 'hours':
            timespan = timedelta(hours=info.time_frame_num)
        elif info.time_frame_type == 'minutes':
            timespan = timedelta(minutes=info.time_frame_num)

        date_start = date_end - timespan
        events = models.AlertEvent.objects.filter(info_id=info, hit_time__range=[date_start, date_end])
        numevents = len(events)
    
        for rule in rules:
            if numevents // rule.numevents > 0:
                if numevents % rule.numevents == 0:
                    time = '至少 %s 个警告 发生在 %s 到 %s 之间\n' % (numevents, str(date_start), str(date_end))
                    message_id = 'id: %d\n'%(info_id)
                    message_body = 'message: %s\n'% info.message

                    text = message_id + time + message_body
                    send_mail(info.title, text , settings.DEFAULT_FROM_EMAIL , [rule.address], fail_silently=False)
                    return JsonResponse({"msg": "An e-mail send!"})

        return JsonResponse({"msg": "Event recived"})
