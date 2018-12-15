# -*- encoding: utf-8 -*-
import sys
import requests
from lxml import etree
from ip_pipeline import Ip_pipeline, IP
from sqlalchemy import or_
printf = sys.stdout.write

def test_proxy(ip,timeout=10):
    '''
    ip 为ORM对象，测试IP是否可用，去除HTTP BASIC AUTH可通过对 测试线程 设置时间限制实现
    :param ip: ip ORM object
    :return: True or False
    '''
    try:
        proxies = {
            'http': 'http://{0}:{1}'.format(ip.ip, ip.port),
            'https': 'https://{0}:{1}'.format(ip.ip, ip.port),
        }
        if ip.proxy_type == 'HTTP':
            resp = requests.get("http://www.baidu.com", proxies = proxies, allow_redirects=False, timeout=timeout)
        elif ip.proxy_type == 'HTTPS':
            resp = requests.get("https://www.baidu.com", proxies=proxies, allow_redirects=False, timeout=timeout)

        if resp.status_code != 200:
            raise Exception("Wrong status code.")

    except Exception,e:
        printf("[PROXY]:" + str(e) + '\n')
        return False

    try:
        resp.encoding = "gbk"
        root = etree.HTML(resp.text)
        title_list = root.xpath("//title/text()")
        if len(title_list)==0:
            raise Exception("No title")
        else:
            title = title_list[0]
        if u'百度' not in title:
            raise Exception("Wrong title")
    except:
        return False
    return True