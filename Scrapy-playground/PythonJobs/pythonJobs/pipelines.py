# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlite3 import dbapi2

class dropPipeline(object):
    def __init__(self):
        self.handler = open("Debug-items.text","w")

    def process_item(self, item, spider):
        self.handler.write(str(item))
        self.handler.write("-"*100)
        if 'python' not in item['title'].lower():
            raise DropItem("title not including 'python' key word")
        else:
            return item     # return item so that following pipelines could process item

    def __del__(self):
        self.handler.close()

class OrmObject(object):
    pass

class sqlitePipeline(object):
    def __init__(self):
        engine = create_engine("sqlite:///Items.db")
        try:
            itemTable = Table('jobs',MetaData(engine),autoload=True)
        except Exception:
            itemTable = Table('jobs',MetaData(engine),
                          Column('id',INTEGER,primary_key=True),
                          Column('title',VARCHAR(30)),
                          Column('city',VARCHAR(10)),
                          Column('company',VARCHAR(100)),
                          Column('location',VARCHAR(100)),
                          Column('url',VARCHAR(60))
                          )
            itemTable.create()
        Session = sessionmaker()
        self.session = Session()
        mapper(OrmObject,itemTable)

    def process_item(self,item,spider):
        # print '-'*70
        # print item
        # print '-' * 70
        already = self.session.query(OrmObject).filter(OrmObject.url==item['url']).count()
        if already==0:
            record = OrmObject()
            for key, value in item.items():
                record.__dict__[key]=value
            self.session.add(record)
        return item

    def close_spider(self,spider):
        self.session.commit()
        self.session.close()
