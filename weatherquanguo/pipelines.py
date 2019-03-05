# -*- coding: utf-8 -*-
import os
import xlsxwriter
import time
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WeatherquanguoPipeline(object):
    def process_item(self, item, spider):
        return item

class WeatherPineline(object):
    def open_spider(self,spider):
        root = "d:/3Weather/"
        path = time.strftime("%Y-%m-%d") + '.xlsx'
        self.workbook = xlsxwriter.Workbook(root + path)
        self.worksheet = self.workbook.add_worksheet()
        self.num0 = 0

    def process_item(self,item,spider):
        self.num0 = self.num0 + 1
        row = 'A' + str(self.num0)
        data = [item['ls_position_name'], item['ls_weather1'], item['ls_weather2'],item['ls_weather3'],item['ls_weather4'],item['ls_weather5'],item['ls_weather6'],item['ls_weather7'],item['ls_weather8'],time.strftime("%Y-%m-%d")]
        self.worksheet.write_row(row, data)
        return item

    def close_spider(self,spider):
        self.workbook.close()

