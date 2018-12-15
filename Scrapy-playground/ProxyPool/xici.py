# -*- encoding: utf-8 -*-
from __future__ import division
from selenium import webdriver
from sqlalchemy import *
from sqlalchemy.orm import *
import datetime
from sqlite3 import dbapi2 as sqlite
from ip_pipeline import Ip_pipeline, IP
import sys
printf = sys.stdout.write

def get_url(num_page):
    for i in xrange(1,num_page+1):
        yield "http://www.xicidaili.com/nn/{0}".format(i)

try:
    n = int(raw_input("Number of pages to crawl:"))
    ip_pipeline = Ip_pipeline()
    f = webdriver.Firefox()
    count = 0
    for url in get_url(n):
        count = count+1
        f.get(url)
        trs = f.find_elements_by_xpath('//table[@id="ip_list"]/tbody/tr[position()>1]')
        num_records = len(trs)
        for row in trs:
            tds = row.find_elements_by_tag_name("td")
            ip_record = IP()
            ip_record.ip = tds[1].text
            printf(ip_record.ip + '\n')
            ip_record.port = tds[2].text
            ip_record.address = tds[3].text
            ip_record.proxy_type = tds[5].text
            ip_record.speed = tds[6].find_element_by_xpath("//div[@title]").get_attribute("title")[:-1]
            ip_record.connection = tds[7].find_element_by_xpath("//div[@title]").get_attribute("title")[:-1]
            ip_record.dur = tds[8].text
            ip_record.check=datetime.datetime.strptime(tds[9].text, "%y-%m-%d %H:%M")
            ip_pipeline.save_proxy(ip_record)
        printf("{0} pages sucessfully crawled!".format(count).center(50,'-'))
    printf("Finish!".center(50, '-'))
except KeyboardInterrupt:
    del ip_pipeline # 触发析构函数关闭数据库？
    printf("Interruptted in {0}th page.".format(count))
