#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hqdvista'

class App(object):
    download_url = ""
    name = ""
    packageName = ""
    version = ""
    update_time = ""
    desc = ""
    vendor = ""

    def __unicode__(self):
        return u"App: vendor %s, packageName %s" % (self.vendor, self.packageName)

    def __str__(self):
        return "App: vendor %s, packageName %s" % (self.vendor, self.packageName)

    def __repr__(self):
        return self.__str__()
