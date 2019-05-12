
# -*- coding: utf-8 -*-

import datetime
from django.utils import timezone
import time

def datetime_add_tz(day_datetime, tz):
    """为datetime添加时区信息"""
    datetime_with_tz = datetime.datetime(day_datetime.year, day_datetime.month, day_datetime.day, tzinfo=tz)

    return datetime_with_tz

def get_range_time(self):

    tz = 'Asia/Shanghai'
    # realtime_between前端之前给时间范围
    dsl_period = self.dsl['period']
    if dsl_period['type'] == 'today':
        now = datetime.datetime.now(tz=tz)
    else:
        now = datetime.datetime.now(tz=tz) - datetime.timedelta(days=1)

    start_time = self.datetime_add_tz(now, tz=now.tzinfo)

    end_day = now + datetime.timedelta(days=1)
    end_time = self.datetime_add_tz(end_day, end_day.tzinfo)

    if dsl_period['type'] == 'today':
        end_time = datetime.datetime.now(tz=tz)

    tz = 'Asia/Shanghai'
    tz = timezone.get_fixed_timezone(8*60)
    now = datetime.datetime.now(tz=tz)
    print(now)
    print(type(datetime_add_tz(now, now.tzinfo)))
    end_time = datetime.datetime.now(tz=tz) + datetime.timedelta(days=1)
    print(datetime_add_tz(end_time, end_time.tzinfo))
    return start_time, end_time




def test_datetime():
    now = datetime.datetime.now()
    # 当前时间
    print(now.isoformat())
    # 转换为时间戳

    dateform = datetime.datetime.fromtimestamp(1429417200.0).strftime('%Y%m%d')
    print(dateform)
    print(now.strftime('%Y%m%d'))
    datetime.datetime(now.year, now.month, now.day)
    print()
    print(now.timetuple())
    a = 1429417200.0
    print(datetime.datetime.utcfromtimestamp(a))

    print(time.mktime(now.date().timetuple()))
    print(int(time.mktime(now.date().timetuple())))

if __name__ == '__main__':

    now = datetime.datetime.now() - datetime.timedelta(days=1)
    start_time = datetime_add_tz(now, tz=now.tzinfo)
    print(now)
    print(start_time)

    from django.utils import timezone

    app_config = dict(
        tz=timezone.get_fixed_timezone(8 * 60),
        time_zone="Asia/Shanghai"
    )

    timestamp = time.mktime(datetime.datetime.now().timetuple())
    print(timestamp)
    print(datetime.datetime.fromtimestamp(timestamp, tz=timezone.get_fixed_timezone(0)))
    print(datetime.datetime.fromtimestamp(timestamp, tz=timezone.get_fixed_timezone(8*60)))
    print(app_config['tz'])