#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qidan.hqd@alibaba-inc.com'
from unittest import TestCase
from downloader.tencent import get_apps
from util import download_applist
class TestTencent(TestCase):
    def test_get_apps(self):
        apps = get_apps()
        download_applist(apps)


