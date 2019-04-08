# encoding: utf-8	


"""
date: 2019/04/01/15/08
"""


"""
加载所需要的包
"""
import os,sys	
import requests	
from bs4 import BeautifulSoup	

'''
创建保存图片的文件夹
'''
sys.path.append(os.path.dirname(os.path.abspath("__file__")))
if not os.path.exists('images'):	
    os.mkdir('images')
else:
    pass

'''
爬取数据
'''
url = "https://xkcd.com/"

while not url.endswith("#"): #如果url不是以#号结尾就一直循环
    res = requests.get(url)	 #使用request.get方法获取网页
    res.raise_for_status()	#检查服务器响应码
    soup = BeautifulSoup(res.text,'lxml') #将得到的网页通过lxml解析成BeautifulSoup对象
    comicItem = soup.select('#comic img') #使用select方法筛选所需要的item
    if comicItem == []:	
        pass	
    else:	
        comicUrl = 'https:'+ comicItem[0].get('srcset')	#获取图片下载链接
        comicUrl = comicUrl.split(" ")[0]	

        res_d = requests.get(comicUrl) #请求图片
        res_d.raise_for_status()	
        imageFile = open(os.path.join('images',os.path.basename(comicUrl)),'wb') #打开图片文件
        for item in res_d.iter_content(10000):
            imageFile.write(item)	#写入图片文件
        imageFile.close()	#关闭图片文件

    preLink = soup.select('a[rel="prev"]')[0] #获取前一页的链接
    url = 'https://xkcd.com/' + preLink.get('href') #更新图片也链接
    print(url) #打印即将获取的网页的url

print("done")