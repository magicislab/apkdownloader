#!/usr/bin/env python
# -*- coding: utf-8 -*-

DOWNLOAD_PREFIX = "/tmp/apks/"
from app import App
import urllib
from multiprocessing.pool import Pool
import os
__author__ = 'hqdvista'
def download_applist(apps):
    """
    :type apps: list(App)
    """
    pool = Pool(processes=10)
    pool.map(download_single_app, apps)
    pool.close()

def download_single_app(app):
    """
    :type app: App
    """
    pth = DOWNLOAD_PREFIX + os.sep + app.vendor
    if not os.path.exists(pth):
        os.makedirs(pth)
    filepath = pth + os.sep + app.packageName + ".apk"
    urllib.urlretrieve(app.download_url, filepath)
    print '''%s downloaded.''' % app.packageName
    return filepath


