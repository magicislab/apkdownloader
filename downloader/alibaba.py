#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hqdvista'
import urllib2
import re
from app import App
import datetime
TAOBAO_APP_URL = "http://app.taobao.com/download/taoApps.htm?pageIndex=4"
DOWNLOAD_RE = r"javascript:openDownloadPanel\(([^\)]+)\);"
def get_apps():
    taoAppPage = urllib2.urlopen(TAOBAO_APP_URL).read()
    apps = re.findall(DOWNLOAD_RE, taoAppPage)
    ret = []
    for appData in apps:
        a = App()
        a.download_url = appData.split(',')[2].strip()[1:-1]
        a.vendor = "Alibaba"
        a.desc = appData.split(',')[1].strip()[1:-1]
        a.packageName =appData.split(',')[5].strip()[1:-1]
        a.update_time = datetime.datetime.now()
        ret.append(a)
    return ret




