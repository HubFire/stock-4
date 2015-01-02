#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = 'cooper'

import traceback
from common import inject
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.exceptions import DontCloseSpider
from xueqiu.spiders.hq_spider import HqSpider
from scrapy.utils.project import get_project_settings
from threading import Thread

class ScrapySpider:
  def __init__(self):
    self.spider = HqSpider()
    self.crawler = crawler = Crawler(get_project_settings())
    crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
    crawler.configure()
    crawler.crawl(self.spider)
    dispatcher.connect(self._dont_close_me, signals.spider_idle)
    self.thread = None
    self._started = False
    self._stopped = False

  def start(self):
    def run():
      try:
        reactor.run()
      except Exception, e:
        print traceback.format_exc()
    if not self._started:
      self._started = True
      self.crawler.start()
      log.start_from_settings(get_project_settings())
      self.thread = Thread(target=run)
      self.thread.start()
    else:
      raise Exception('spider has already started.')

  def stop(self):
    if not self._started:
      raise Exception('spider not started.')
    elif self._stopped:
      raise Exception('spider has already stopped')
    else:
      self._stopped = True
      self.crawler.stop()

  def _dont_close_me(self, spider):
    raise DontCloseSpider("..I prefer live spiders.")

