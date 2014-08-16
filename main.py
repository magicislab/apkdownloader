#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cmd
__author__ = 'hqdvista'
import util
import os


class AppDownloaderCmd(cmd.Cmd):
    DOWNLOAD_PATH = "/tmp/"
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.cache_pool = {}
        self.cfg = {'download_path': AppDownloaderCmd.DOWNLOAD_PATH}

    def do_help(self, arg):
        if arg == "":
            print '''input vendor name to download their apps'''
        else:
            cmd.Cmd.do_help(self, arg)

    def do_quit(self, args):
        raise SystemExit

    def do_download(self, args):
        """
        Download apps from vendor. Stored in path specified by config download_path
        """
        if args == "":
            print '''Error: please provide a vendor to download'''
        else:
            apps = self.__getAppInfos(args)
            util.DOWNLOAD_PREFIX = self.cfg.get('download_path', AppDownloaderCmd.DOWNLOAD_PATH)
            print '''Downloading %d apps''' % len(apps)
            util.download_applist(apps)
            print '''Download completed.'''

    def __getAppInfos(self, vendor):
        if vendor in self.cache_pool:
            return self.cache_pool[vendor]
        else:
            try:
                downloader = __import__("downloader."+vendor, fromlist=[''])
                apps = downloader.get_apps()
                self.cache_pool[vendor] = apps
                return apps
            except ImportError:
                print '''Error: downloader for %s not found''' % vendor
                return []

    def do_clearcache(self, vendor):
        """
        Clear apps cache from vendor
        """
        self.cache_pool.pop(vendor,None)
        print "Cache for " + vendor + " cleared"

    def do_showapps(self, args):
        """
        Show apps from vendor. Input format: vendor
        """
        apps = self.__getAppInfos(args)
        print '\n'.join([app.packageName for app in apps])

    def do_ds(self, args):
        """
        Download single app. Input format: vendor, pkgName
        """
        if len(args.split()) != 2:
            print '''Error: input format: ds vendor pkgName'''
            return False
        vendor, pkgName = args.split()
        apps = self.__getAppInfos(vendor)
        for app in apps:
            if app.packageName == pkgName:
                print "Downloading app for " + pkgName + " ..."
                util.DOWNLOAD_PREFIX = self.cfg.get('download_path', AppDownloaderCmd.DOWNLOAD_PATH)
                filepath = util.download_single_app(app)
                print "Done. Saved to %s. Total Size: %d bytes." % (filepath, os.path.getsize(filepath))
                return False
        print "Oops, %s of %s not found." % (vendor, pkgName)
        return False

    def do_cfg(self, args):
        """
        modify cfg for downloader, e.g. download_path. Input format: key value
        """
        if len(args.split()) != 2:
            print '''Error: input format: cfg key value'''
            return False
        key, value = args.split()
        self.cfg[key] = value
        return False

if __name__ == '__main__':
    downloader = AppDownloaderCmd()
    downloader.prompt = '> '
    downloader.cmdloop("Staring Downloader...")
