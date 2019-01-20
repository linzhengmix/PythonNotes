# -*- coding:utf-8 -*-

# /**
# 
# Author:      LinZheng
# Copyright    All Rights Reserved
# DateTime:    2016-11-09 11:13:13
# Description: python class practise
# 
# **/
#from imp import reload

import requests
import re
from bs4 import BeautifulSoup
import os
import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')


class MeiPic():
    """docstring for MeiPic"""

    def request(self, url):
        content = requests.get(url)
        return content

    def all_url(self, url):
        html = self.request(url)
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
        #print all_a
        for a in all_a:
            # print a
            title = a.get_text()
            href = a['href']
            regex = r'http://www.mzitu.com/(\d+)'
            pattern = re.compile(regex)
            m = pattern.match(href).group(1)
            # print m
            self.mkdir(m)
            path = str(m)
            parent_path = os.getcwd()
            paths = os.path.join(parent_path, path)
            os.chdir(paths)
            self.html(href)
            os.chdir(parent_path)

    def mkdir(self, path):
        path = path.strip()
        parent_path = os.getcwd()
        isExists = os.path.exists(os.path.join(parent_path, path))
        # print isExists
        # print os.getcwd()
        if not isExists:
            print(u'Creating a new file...')
            os.makedirs(os.path.join(parent_path, path))
            return True
        else:
            return False

    def img(self, page_url):
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url)

    def save(self, img_url):
        name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()

    def html(self, href):
        html = self.request(href)
        max_span = BeautifulSoup(html.text, 'lxml').find_all('span')[10].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url)


MeiPic = MeiPic()
MeiPic.all_url('http://www.mzitu.com/all')


