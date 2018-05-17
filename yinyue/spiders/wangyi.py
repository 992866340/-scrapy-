# -*- coding: utf-8 -*-
import scrapy
from yinyue.items import YinyueItem
import json
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['163.com']
    song_name = input('请输入你要下载的音乐:')
    def start_requests(self):
        item = YinyueItem()
        url = 'http://music.163.com/api/search/pc'
        data = {
            's' : self.song_name,
            'offset' : '0',
            'limit' : '1',
            'type' : '1'
        }
        yield scrapy.FormRequest(url,callback=self.getjson,formdata=data,meta={'item':item})
    def getjson(self,response):
        item = response.meta['item']
        str = json.loads(response.text)
        print('*'*100)
        item['music_id'] = str['result']['songs'][0]['id']
        item['music_singer'] = str['result']['songs'][0]['artists'][0]['name']
        item['music_name'] = str['result']['songs'][0]['name']
        item['music_img'] = str['result']['songs'][0]['album']['picUrl']
        item['music_url'] = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(item['music_id'])
        print(item['music_url'])
        yield item