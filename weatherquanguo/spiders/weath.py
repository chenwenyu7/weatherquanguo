# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import os
from weatherquanguo.items import WeatherquanguoItem
import time

class WeathSpider(scrapy.Spider):
    name = 'weath'
    #allowed_domains = ['weather.com.cn']
    base_url = "http://www.weather.com.cn/weather1d/101"
    url_list = []
    province_num = 5
    while (province_num < 6):
        flag = True
        city_num = 1
        while (city_num < 3):
            position_num = 1
            while (position_num < 5):
                try:
                    num_str = str(province_num).zfill(2) + str(city_num).zfill(2) + str(position_num).zfill(2)
                    url = base_url + num_str + ".shtml"
                    url_list.append(url)
                    position_num += 1
                except:
                    break
            if (flag == False and position_num == 1):
                break
            city_num += 1
            pass
        if (flag == False and position_num == 1 and city_num == 1):
            break
        province_num += 1
    #start_urls = url_list
    def start_requests(self):
        for url1 in WeathSpider.url_list:
            yield scrapy.Request(url = url1,callback=self.parse)

    def parse(self, response):
        #定义收集的列表
        ls_position_name = []
        ls_weather1 = []
        ls_weather2 = []
        ls_weather3 = []
        ls_weather4 = []
        ls_weather5 = []
        ls_weather6 = []
        ls_weather7 = []
        ls_weather8 = []
        data = WeatherquanguoItem()
        soup = BeautifulSoup(response.body, 'html.parser')
        res_data = soup.findAll('script')
        weather_data = res_data[4]
        # fullName = getPositionName(soup, num)
        for x in weather_data:
            weather1 = x
            index_start = weather1.find("{")
            index_end = weather1.find(";")
            weather_str = weather1[index_start:index_end]
            weather = eval(weather_str)
            weather_dict = weather["od"]
            list1 = list(reversed(weather["od"]["od2"]))
            for i in range(1, len(weather["od"]["od2"])):
                ls_position_name.append(weather_dict["od1"])
                ls_weather1.append(list1[i]['od21'])
                ls_weather2.append(list1[i]['od22'])
                ls_weather3.append(list1[i]['od23'])
                ls_weather4.append(list1[i]['od24'])
                ls_weather5.append(list1[i]['od25'])
                ls_weather6.append(list1[i]['od26'])
                ls_weather7.append(list1[i]['od27'])
                ls_weather8.append(list1[i]['od28'])

        for i,j,k,l,m,n,o,p,q in zip(ls_position_name,ls_weather1,ls_weather2,ls_weather3,ls_weather4,ls_weather5,ls_weather6,ls_weather7,ls_weather8):
            data['ls_position_name']=i
            data['ls_weather1'] = j
            data['ls_weather2'] = k
            data['ls_weather3'] = l
            data['ls_weather4'] = m
            data['ls_weather5'] = n
            data['ls_weather6'] = o
            data['ls_weather7'] = p
            data['ls_weather8'] =q
            yield data
