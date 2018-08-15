import xadmin

from .models import AlertInfo, AlertRule, AlertEvent


class AlertInfoAdmin(object):
    '''信息'''
    
    list_display = ['info_id','title','message','time_frame_type','time_frame_num','update_time', 'create_time']
    search_fields =  ['info_id','title','message','time_frame_type','time_frame_num']
    list_filter =  ['info_id','title','message','time_frame_type','time_frame_num','update_time', 'create_time']


class AlertRuleAdmin(object):
    '''规则'''
    
    list_display = ['rule_id', 'info_id', 'alert_type', 'address', 'numevents']
    search_fields = ['rule_id', 'alert_type', 'address', 'numevents']
    list_filter = ['rule_id', 'info_id', 'alert_type', 'address', 'numevents']


class AlertEventAdmin(object):
    '''事件'''
    list_display = ['event_id', 'info_id', 'hit_time']
    search_fields = ['event_id']
    list_filter = ['event_id', 'info_id', 'hit_time']



# 将管理器与model进行注册关联
xadmin.site.register(AlertInfo, AlertInfoAdmin)
xadmin.site.register(AlertRule, AlertRuleAdmin)
xadmin.site.register(AlertEvent, AlertEventAdmin)
