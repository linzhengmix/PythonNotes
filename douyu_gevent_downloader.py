
import urllib.request
import gevent

from gevent import monkey

monkey.patch_all()

def getImageUrl():
    pass

def downloader(filename,url):
    req = urllib.request.urlopen(url)
    content = req.read()

    with open(filename,"wb") as f:
        f.write(content)

def main():
    gevent.joinall([
        gevent.spawn(downloader,"1.jpg","https://rpic.douyucdn.cn/live-cover/roomCover/2018/12/16/a9df2bf65fcd5f159b1326b3e591cd51_big.jpg"),
        gevent.spawn(downloader,"2.jpg","https://rpic.douyucdn.cn/live-cover/appCovers/2019/01/08/6217770_20190108004245_small.jpg"),
        gevent.spawn(downloader,"3.jpg","https://rpic.douyucdn.cn/live-cover/appCovers/2018/12/19/6097308_20181219230319_small.jpg")
    ])


if __name__ == '__main__':
    main()