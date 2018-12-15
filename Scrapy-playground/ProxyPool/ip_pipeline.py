#! -*- encoding:utf-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import *
import pymysql
import sys
printf = sys.stdout.write


class IP(object):
    pass

class Ip_pipeline(object):
    '''
    session
    current       current row(read)
    offset        for next iteration
    count_ips     total record retried in __init__
    get_proxy     get one ip record and move offset for next iter
    '''


    def __init__(self):
        self.engine = create_engine("mysql+pymysql://root:root@localhost/proxies?charset=utf8")
        try:
            self.iptable = Table('ips', MetaData(self.engine), autoload=True)
        except Exception:
            self.iptable = Table('ips', MetaData(self.engine),
                            Column('ip', VARCHAR(16), primary_key=True),
                            Column('port', Integer, nullable=False),
                            Column('address', VARCHAR(20)),
                            Column('proxy_type', VARCHAR(5)),
                            Column('speed', FLOAT),
                            Column('connection', FLOAT),
                            Column('dur', TEXT),
                            Column('check', DateTime(timezone="Asia/Shanghai"))
                            )
            self.iptable.create()

        self.Session=sessionmaker(bind=self.engine)
        self.session = Session()
        mapper(IP,self.iptable)
        self.count_ips = self.session.query(IP).count()


    def get_proxy(self, proxy_type): # proxy_type = 'HTTP' or 'HTTPS'
        while True:
            query = self.session.query(IP).filter(IP.proxy_type==proxy_type).yield_per(10)
            for ip in IP:
                yield [ip.ip,ip.port]
        # try:
        #     ip = self.session.query(IP.ip,IP.port).filter(IP.proxy_type==proxy_type).limit(1).offset(self.offset).one()
        # except Exception,e:
        #     self.offset=0
        #     ip = self.session.query(IP.ip, IP.port).filter(IP.proxy_type == proxy_type).limit(1).offset(self.offset).one()
        # finally:
        #     self.offset += 1

    def save_proxy(self, proxy_item):  # proxy_item 为IP 对象
        if self.session.query(IP).filter(IP.ip == proxy_item.ip).count() != 0:  # 去重
            printf("Already in db.\n")
            return None
        try:
            self.session.add(proxy_item)
            self.session.commit()  # have to commit here or in the next iteration, query won't be able to find the item added
        except:
            self.session.rollback()
            return None

    def delete_proxy(self, ip):
        try:
            ip = self.session.query(IP).filter(IP.ip==ip).delete()
            self.session.commit()
            printf("Deleted.")
        except Exception, e:
            printf("Proxy not in db.")

    def __del__(self):
        self.session.close()
	printf("\ncommit by ip pipeline\n".center(50,"-")+'\n')
