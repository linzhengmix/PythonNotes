#coding=utf-8


import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
# from items import DingdianItem
import requests
import urllib


# headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
class Myspider(scrapy.Spider):
 
    name = 'dingdian'
    allowed_domains = ['23us.com']
    bash_url = 'http://www.23us.com/class/'
    bashurl = '.html'
 
    def start_requests(self):
        for i in range(1, 10):
            url = self.bash_url + str(i) + '_1' + self.bashurl
            yield Request(url, self.parse)
        yield Request('http://www.23us.com/quanben/1', self.parse)
 
    def parse(self, response):
        url = response.url
        max_num = BeautifulSoup(urllib.urlopen(url).read(),'lxml').find('div',class_ = 'pagelink').find_all('a')[-1].get_text()
        # print(Soup.find_all('li'))
        # max_num = BeautifulSoup(response.text(),'lxml').find('div',class_ = 'pagelink').find_all('a')[-1].get_text()
        # print(max_num)
        bashurl = str(response.url)[:-7]
        # print(bashurl)
        for num in range(1,int(max_num) + 1):
            url = bashurl + '_' + str(num) + self.bashurl
            yield Request(url, self.get_name)

    def get_name(self,response):
        url = response.url
        html = urllib.urlopen(url).read()
        tds = BeautifulSoup(urllib.urlopen(url).read(),'lxml').find_all('tr',bgcolor='#FFFFFF')
        for td in tds:
            novelname = td.find_all('a')[1].get_text()
            # print(novelname)
            novelurl = td.find('a')['href']
            yield Request(novelurl, callback = self.get_chapter,meta = {'name': novelname,'url': novelurl})

    def get_chapter(self,response):
        item = DingdianItem()
        # item['name'] = str(reponse.meta['name']).replace('\xa0','')
        # item['url'] = str(reponse.meta['url'])
        url = response.url
        print(url)
        category = BeautifulSoup(urllib.urlopen(url).read(),'lxml').find('table').find('a').get_text()
        print(category)
        author = BeautifulSoup(urllib.urlopen(url).read(),'lxml').find('table').find('td').get_text().replace('\xa0','')
        print(author)
        # bash_url = BeautifulSoup(urllib.urlopen(url).read(),'lxml').find('p',class_ = 'btnlinks').find('a',class_ = 'read')['href']
        #name_id = str(bash_url)[-6:-1].replace('/','')
        #item('category') = str(category).replace('/','')
        #item('author') = str(author).replace('/','')
        #item('name_id') = name_id
        return item


