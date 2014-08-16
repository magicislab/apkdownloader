#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'hqdvista'

import json
import urllib2
import logging
from app import App
SOURCE_URL = "http://sj.qq.com/myapp/cate/appList.htm?orgame=1&categoryId=-10&pageSize=20&pageContext={count}"

VENDOR = "Tencent"
def get_apps():
    i = 0
    apps = []
    while True:
        pageApp = __parseMyappJson(urllib2.urlopen(SOURCE_URL.format(count=i*20)).read())
        if len(pageApp) == 0:
            break
        else:
            apps.extend(pageApp)
        i += 1
        print i
    print len(apps)
    return apps

def __parseMyappJson(jstr):
    ret = []
    jobj = json.loads(jstr)
    if jobj['count'] == 0:
        return ret
    else:
        objs = jobj['obj']
        for appResp in objs:
            app = App()
            app.desc = appResp.get("editorIntro", "")
            app.download_url = appResp['apkUrl']
            app.packageName = appResp.get('pkgName',"")
            app.name = appResp.get("appName","")
            app.update_time = appResp.get("apkPublishTime","")
            app.vendor = VENDOR
            ret.append(app)
    return ret
