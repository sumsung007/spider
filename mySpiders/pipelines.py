# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import time
import mySpiders.utils.log as logging
from mySpiders.utils.hash import toMd5
from mySpiders.sql.mysql import Mysql
from mySpiders.utils.http import requstDistinct
from config import db_host,db_user,db_password,db_name,db_table_name


class SpidersPipeline(object):
    def process_item(self, item, spider):
        return item


class CSDNPipeline(object):

    def __init__(self):
        self.file = codecs.open('res.json', mode='a+', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode('unicode_escape'))

        return item


class BsbdjPipeline(object):

    def __init__(self):
        self.file = codecs.open('bsbdj_res.json', mode='a+', encoding="utf-8")

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.decode('unicode_escape'))


class XmlFeedPipeline(object):

    def __init__(self):

        config = {'host':db_host,'user':db_user,'passwd':db_password}
        database = db_name
        self.db =  Mysql(config,database)
        self.tableName = db_table_name

    def process_item(self, item, spider):

        rule_id = item['rule_id']
        public_time = int(time.time())
        create_time = int(time.time())
        for index,title in enumerate(item['title']):
            
            uniqueCode = toMd5(item['source_url'][index])
            if not requstDistinct(uniqueCode) :
                logging.info("-----------%s----has exists----------" % item['source_url'][index])
                continue

            if index<len(item['img_url']) and item['img_url'][index]:
                img_url = json.dumps(item['img_url'][index])
            else:
                img_url = ''

            if index<len(item['description']) and item['description'][index]:
                description = item['description'][index]
            else:
                continue           
            
            title = title.decode('utf8')[0:255].encode('utf8')

            insertData = {
                'source_url'  : item['source_url'][index],
                'unique_code' : uniqueCode,
                'rule_id'     : rule_id,                
                'title'       : title,      
                'description' : description,
                'img_url'     : img_url,
                'public_time' : public_time,
                'create_time' : create_time
            }
            self.db.insert(self.tableName,insertData)
        return True