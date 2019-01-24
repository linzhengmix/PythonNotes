# encoding: utf-8

"""
author:Zhenglin
email:mixfruitszu@gmail.com
time: 2019/01/19/00/29

"""

import threading
import time

def test1():
    while True:
        print("1--------\n")
        time.sleep(1)


def test2():
    while True:
        print("2--------\n")
        time.sleep(1)

def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()