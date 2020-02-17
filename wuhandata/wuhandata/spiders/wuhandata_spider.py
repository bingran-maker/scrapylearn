# -*- coding: utf-8 -*-
import scrapy


class WuhandataSpider(scrapy.Spider):
    name = 'wuhandata'#应用名称
    #允许爬取的域名
    #allowed_domains = ['https://voice.baidu.com/act/newpneumonia/newpneumonia']
    allowed_domains = ['https://news.qq.com//zt2020/page/feiyan.htm']
    #起始爬取的URL
    #start_urls = ['http://https://voice.baidu.com/act/newpneumonia/newpneumonia/']
    start_urls=['https://news.qq.com//zt2020/page/feiyan.htm']

    # 访问起始URL并获取结果后的回调函数，该函数的response参数就是向起始的url发送请求后
    # 获取的响应对象.该函数返回值必须为可迭代对象或者NUll
    def parse(self, response):
        print("11111111111111111111111111111111")
        # "count___3GCdh"
        # a= response.xpath('//p[@id="certainTotal"]//text()').extract()
        a = response.xpath('//div[@class="number"]')
        print(a)
        print(len(a))


