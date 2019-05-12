#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import time
from django.utils import timezone


def test_timeformat():
    now = datetime.datetime.now()
    timestamp = time.mktime(now.timetuple())
    print("timestamp: ", int(timestamp))

    parse_date = datetime.datetime.fromtimestamp(timestamp)
    print(parse_date)

    # 格式转换，转换为本地时区
    date_time_format = datetime.datetime.strftime(parse_date, '%Y%m%dT%H%M')
    print(date_time_format)

    # 格式转换，转换为UTC时区的格式
    tz = timezone.get_fixed_timezone(0)
    date_time_utc = datetime.datetime.fromtimestamp(timestamp, tz=tz)
    print(date_time_utc)



def get_timezones():
    shanghai = dict(
        tz=timezone.get_fixed_timezone(8 * 60),
        time_zone="Asia/Shanghai"
    )

    landon = dict(
        tz=timezone.get_fixed_timezone(0),
        time_zone="Europe/London"
    )

    return (shanghai, landon)

def datetime_add_tz(day_datetime, tz):
    """为datetime添加时区信息"""
    datetime_with_tz = datetime.datetime(day_datetime.year, day_datetime.month, day_datetime.day, tzinfo=tz)
    return datetime_with_tz

def test_yesterday():
    tz=timezone.get_fixed_timezone(8 * 60)
    now = datetime.datetime.now(tz=tz) - datetime.timedelta(days=1)
    start_time = datetime_add_tz(now, tz=now.tzinfo)
    end_day = now + datetime.timedelta(days=1)
    end_time = datetime_add_tz(end_day, end_day.tzinfo)
    print(start_time, end_time)

def tmp():
    now = datetime.datetime.now()
    yesterday = now - datetime.timedelta(days=2)

    print(time.mktime(yesterday.timetuple()), time.mktime(now.timetuple()))
    print(datetime.datetime.fromtimestamp(1554966000))


if __name__ == '__main__':
    tz = timezone.get_fixed_timezone(0)

    print(datetime.datetime.now(tz=tz))

    now = datetime.datetime.fromtimestamp(1555330198, tz=tz)
    print(now)
    now_8 = datetime.datetime.fromtimestamp(1555330198, tz=timezone.get_fixed_timezone(8*60))
    print(now_8)

    print(datetime.datetime.utcfromtimestamp(1555330198))

    date = datetime.datetime.fromtimestamp(1555171200, tz=tz)
    print(datetime.datetime.utcfromtimestamp(1555171200))
    print(datetime.datetime.fromtimestamp(1555171200).isoformat())
    print(datetime.datetime.now(tz=tz))

    timestamp = time.mktime(datetime.datetime(2019, 4, 14, tzinfo=tz).timetuple())
    print(date)
    print(timestamp)