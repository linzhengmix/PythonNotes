# -*- encoding: utf-8 -*-
import requests
import sys
import threading
from lxml import etree
import datetime
from ip_pipeline import Ip_pipeline, IP
from test_proxy import test_proxy
printf = sys.stdout.write

pipeline = Ip_pipeline()

headers = {'Host': 'www.xicidaili.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Referer': 'http://www.xicidaili.com/',
'Connection': 'keep-alive',
           }

class Test(threading.Thread):
    def __init__(self,ip,resource):
        super(Test, self).__init__()
        self.ip = ip
        self.pipeline = pipeline
        self.valid = None

    def run(self):
        self.valid = test_proxy(self.ip)
        resource.release()

resource = threading.Semaphore(5)
num_page = int(raw_input("Number of pages to crawl:"))

for i in xrange(1, num_page+1):
    url = "http://www.xicidaili.com/nn/{0}".format(i)
    resp = requests.get(url,headers=headers)
    tree = etree.HTML(resp.text)
    trs = tree.xpath("//tr[position()>1]")
    threads = list()
    for tr in trs:
        ip_record = IP()
        ip_record.ip = tr.xpath("td")[1].text.decode("utf-8")
        printf(ip_record.ip + '\n')
        ip_record.port = int(tr.xpath("td")[2].text)
        address_list = tr.xpath("td[4]/descendant::text()")
        address = reduce(lambda x,y: x+y, address_list)
        ip_record.address = address.strip()
        ip_record.proxy_type = tr.xpath("td")[5].text.decode("utf-8")
        ip_record.speed = tr.xpath("td")[6].xpath("div/@title")[0][:-1]
        ip_record.connection = tr.xpath("td")[7].xpath("div/@title")[0][:-1]
        ip_record.dur = tr.xpath("td")[8].text
        ip_record.check = datetime.datetime.strptime(tr.xpath("td")[9].text, "%y-%m-%d %H:%M")
        threads.append(Test(ip_record,resource))

    for thread in threads:
        resource.acquire()
        thread.start()

    for thread in threads:
        thread.join()      #TODO Might get stuck here when encountering HTTP BASIC AUTH
        printf(str(thread.ip.ip) + ": " + str(thread.ip.port) + "\n")
        if thread.valid == True:
            pipeline.save_proxy(thread.ip)
            printf("Success\n")
        else:
            printf("Fail\n")
        printf("-"*30)