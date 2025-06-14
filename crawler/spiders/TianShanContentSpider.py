import scrapy
from scrapy.selector import Selector

'''
天山网维语板块爬虫

从link.txt中读取对应连接进行爬虫
爬虫内容保存在content.txt

'''

class TianShanContentSpider(scrapy.Spider):
    name = "tianshancontent"
    start_urls = []  # You would likely populate these from 'link.txt'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content_file = open("content.txt", 'w', encoding='utf-8')

    def closed(self, reason):
        self.content_file.close()

    def parse(self, response):
        selector = Selector(response)
        # Implement your parsing logic here and write to self.content_file
        pass