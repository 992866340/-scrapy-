# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import pymysql
import os
class YinyuePipeline(object):
    def open_spider(self,spider):
        self.db = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', password = '123456', db = '网易云音乐', charset = 'utf8')
        self.db.set_charset('utf8')
        self.cursor = self.db.cursor()
    def process_item(self, item, spider):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        }
        sql = 'insert into music (music_name,music_singer,music_id,music_img,music_url) values ("{}","{}","{}","{}","{}");'.format(item['music_name'],item['music_singer'],item['music_id'],item['music_img'],item['music_url'])
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()
        r = requests.get(item['music_url'],headers=headers)
        filename = item['music_singer'] + '-' + item['music_name'] + '.mp3'
        dirpath = r'D:\音乐'
        filepath = os.path.join(dirpath,filename)
        with open(filepath,'wb') as fp:
            fp.write(r.content)
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()