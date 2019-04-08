# encoding: utf-8	

 """	
date: 2019/04/01/15/08	
 """	
import os,sys	
import requests	
from bs4 import BeautifulSoup	

 sys.path.append(os.path.dirname(os.path.abspath("__file__")))	
if not os.path.exists('images'):	
    os.mkdir('images')	
else:	
    pass	

 url = "https://xkcd.com/"	

 while not url.endswith("#"):	
    res = requests.get(url)	
    res.raise_for_status()	
    soup = BeautifulSoup(res.text,'lxml')	
    comicItem = soup.select('#comic img')	
    if comicItem == []:	
        pass	
    else:	
        comicUrl = 'https:'+ comicItem[0].get('srcset')	
        comicUrl = comicUrl.split(" ")[0]	

         res_d = requests.get(comicUrl)	
        res_d.raise_for_status()	
        imageFile = open(os.path.join('images',os.path.basename(comicUrl)),'wb')	
        for item in res_d.iter_content(10000):	
            imageFile.write(item)	
        imageFile.close()	

     preLink = soup.select('a[rel="prev"]')[0]	
    url = 'https://xkcd.com/' + preLink.get('href')	
    print(url)	

 print("done")