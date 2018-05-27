# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from logo.items import LogoItem
from scrapy.contrib.linkextractors import LinkExtractor

class LogoSpider(CrawlSpider):
    name = 'logo'
    allowed_domains = ['pcauto.com.cn']
    start_urls = ['http://www.pcauto.com.cn/zt/chebiao/guochan/']

    rules = (
            Rule(LinkExtractor(allow=(r'http://www.pcauto.com.cn/zt/chebiao/.*?/$')), callback='parse_page'),
        )


    def parse_page(self, response):
        # print(response.text)
        sel = Selector(response)
        # print(sel)
        country = "".join(sel.xpath('//div[@class="th"]/span[@class="mark"]/a/text()').extract())
        # carname = sel.xpath('//div[@class="dPic"]/i[@class="iPic"]/a/img/@alt').extract()
        # imageurl = sel.xpath('//div[@class="dPic"]/i[@class="iPic"]/a/img/@src').extract()
        # item=LogoItem(country=country, carname=carname, imageurl=imageurl)
        # yield item

        carnames = sel.xpath('//div[@class="dPic"]/i[@class="iPic"]/a/img/@alt').extract()
        for carname in carnames:
            imageurl= sel.xpath('//div[@class="dPic"]/i[@class="iPic"]/a/img[@alt="'+carname+'"]/@src').extract()
            # print(country, carname, imageurl)
            item = LogoItem(country=country, carname=carname, imageurl=imageurl)
            yield item


# class LogospiderSpider(scrapy.Spider):    #抓取单一页面，没有rules
#     name = 'LogoSpider'
#     allowed_domains = ['pcauto.com.cn']
#     start_urls = ['http://www.pcauto.com.cn/zt/chebiao/guochan/']
#     rules = (
#         Rule(LinkExtractor(allow=(r'http://www.pcauto.com.cn/zt/chebiao/.*?/$')), callback='parse')
#     )
#     def parse(self, response):
#         print(response.text)
