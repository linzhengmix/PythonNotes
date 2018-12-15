# -*- encoding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlite3 import dbapi2 as sqlite
import urllib.request, urllib.parse, urllib.error
import json
import socket
import sys



class Item(object):
    pass

class City(object):
    pass

class Geo_job(object):
    pass

class ItemDb(object):
    def __init__(self):
        self.current = 0
        engine = create_engine("sqlite:////../data/Items.db",encoding="utf-8")
        itemTable = Table('jobs',MetaData(engine),autoload = True)
        try:
            cityTable = Table('cities',MetaData(engine),autoload=True)
        except:
            cityTable = Table('cities',MetaData(engine),
                              Column('city',VARCHAR(20),primary_key=True),
                              Column('count',Integer,default=0),
                              Column('lat',FLOAT,nullable=True),
                              Column('lon',FLOAT,nullable=True)
                              )
            cityTable.create()
        Session = sessionmaker()
        self.session = Session()
        mapper(Item,itemTable)
        mapper(City,cityTable)

        try:
            geoTable = Table('geo_job',MetaData(engine),autoload=True)
        except Exception:
            geoTable = Table('geo_job',MetaData(engine),
                             Column('id',INTEGER,primary_key=True),
                             Column('id_foreign',ForeignKey(Item.id)),
                             Column('lat',FLOAT),
                             Column('lon',FLOAT)
                             )
            geoTable.create()
        mapper(Geo_job,geoTable)
        self.count = self.session.query(Item).count()

    def __del__(self):
        self.session.close()

    def __next__(self):
        if self.current < self.count:
            item = self.session.query(Item).limit(1).offset(self.current).one()
            self.current += 1
            if item == None:
                raise StopIteration
            return item

    def __iter__(self):
        return self

def get_geo_GCJ(location,key):
    api = "http://restapi.amap.com/v3/geocode/geo?"
    try:
        fhand = urllib.request.urlopen( api + urllib.parse.urlencode({'key':key,'address':location}) )
        response = fhand.read().decode("utf-8")
        response = json.loads(response)
    except Exception as e:
        print("Geode connection fail")
        print(e)
        return None,None
    try:
        geo_list = response['geocodes'][0]['location'].split(',')
        lon = float(geo_list[0])
        lat = float(geo_list[1])
        return lat,lon
    except Exception as e:
        return None,None

def gcj_to_WGS(lat_gcj,lon_gcj):
    if lat_gcj!= None and lon_gcj!=None:
        try:
            api = 'http://api.zdoz.net/transgps.aspx?'
            fhand = urllib.request.urlopen( api + urllib.parse.urlencode({'lat':lat_gcj,'lng':lon_gcj}) )
            response = fhand.read().decode("utf-8")
            response = json.loads(response)
        except Exception as e:
            print("ZODZ connection fail")
            print(e)
            return None,None
    else:
        response = dict()

    try:
        lat_wgs = response['Lat']
        lon_wgs = response['Lng']
        return lat_wgs,lon_wgs
    except Exception as e:
        return None,None

if __name__ == '__main__':
    socket.setdefaulttimeout(10)
    city_err_hand = open('City_Failed.txt',"a")
    job_err_hand = open("Job_Failed.txt","a")
    key = input("Please input Geode aip key: ")
    db = ItemDb()
    for item in db:
        city_str = item.city.split('-')[0]
        job_location = item.location
        job_url = item.url
        job_id = item.id

        try:
            geoJob = db.session.query(Geo_job).filter(Geo_job.id_foreign == job_id).one()   # already in geoJob table
        except:
            geoJob = Geo_job()
            lat_job_gcj, lon_job_gcj = get_geo_GCJ(job_location, key)
            lat_job_wgs, lon_job_wgs = gcj_to_WGS(lat_job_gcj,lon_job_gcj)
            if lat_job_wgs == None or lon_job_wgs == None:
                job_err_hand.write(item.url+'\n')
                print("Job loacation retrieving fail:")
                print(item)
                print("Record written to geo_job table without lat or lon.")
                print('-' * 50)
            geoJob.id_foreign = job_id
            geoJob.lat, geoJob.lon = lat_job_wgs, lon_job_wgs
            db.session.add(geoJob)
        else:
            print("skip".center(70,'-'))
            continue        # skip city count

        try:
            cityObj = db.session.query(City).filter(City.city==city_str).one()          # record already exit, lat and lon assumed to set
            cityObj.count += 1
            db.session.commit()
        except Exception:
            cityObj = City()   # record not in db, add a new record, fields: city, count, lat, lon
            cityObj.city = city_str
            cityObj.count = 1
            lat_gcj, lon_gcj = get_geo_GCJ(city_str,key)
            lat_wgs, lon_wgs = gcj_to_WGS(lat_gcj,lon_gcj)  # Chinese positioning standard GCJ to International Standard WGS
            if lat_wgs==None or lon_wgs==None:
                city_err_hand.write(item.url+'\n')
                print("City location retrieving fail:")
                print(item)
                print("City written to cities table without lat or lon.")
                print('-'*50)
            cityObj.lat, cityObj.lon = lat_wgs, lon_wgs
            db.session.add(cityObj)

        db.session.commit()
        print("iteration for: " + item.url)
        print('-'*70)
        city_err_hand.flush()
        job_err_hand.flush()
    city_err_hand.close()
    job_err_hand.close()
