from app import App

__author__ = 'hqd'

import base64
import urllib2
import json
SOURCE_URL = "http://android.myapp.com/myapp/searchAjax.htm?kw=com.jd&pns={pnsb64}"
MAX_PAGE_CNT = 3
filters = ("com.jd.", "com.jingdong.")
VENDOR = "JingDong"

def get_apps():
    ret = []
    for i in range(MAX_PAGE_CNT):
        pagestr = str(i*10)
        url = SOURCE_URL.format(pnsb64 = base64.b64encode(pagestr))
        resp = json.loads(urllib2.urlopen(url).read())
        appdetails = resp['obj']['appDetails']
        for appdetail in appdetails:
            app = App()
            app.desc = appdetail["description"]
            app.download_url = appdetail["apkUrl"]
            app.packageName = appdetail["pkgName"]
            app.name = appdetail["appName"]
            app.update_time = appdetail["apkPublishTime"]
            app.vendor = VENDOR
            if app.packageName.startswith(filters):
                ret.append(app)
    return ret