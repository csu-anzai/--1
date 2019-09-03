# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DdPipeline(object):
    def process_item(self, item, spider):
        #连接数据库
        conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="dd")
        #将得到的数据用列表显示出来
        for i in range(0, len(item["title"])):
            title = item["title"][i]
            link = item["link"][i]
            comment = item["comment"][i]
            sql = "insert into book(title,link,comment) values('"+title+"','"+link+"','"+comment+"')"
            conn.query(sql)
        conn.close()
        return item
