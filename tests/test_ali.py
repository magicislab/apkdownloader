#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hqdvista'
import unittest
from downloader.alibaba import get_apps
class TestAli(unittest.TestCase):
    def test_download(self):
        print get_apps()

