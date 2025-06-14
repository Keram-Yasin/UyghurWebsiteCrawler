import scrapy
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url

'''
天山网维语板块爬虫

列表连接保存在link.txt
标题保存在title.txt

'''

class TianShanSpider(scrapy.Spider):
    name = "tianshan"
    allowed_domains = ["uy.ts.cn"]
    link_file = 'link.txt'
    title_file = "title.txt"
    start_urls = []

    urls = {
        "http://uy.ts.cn/news/node_899": '100',
        "http://uy.ts.cn/news/node_900": '100',
        "http://uy.ts.cn/news/node_901": '100',
        "http://uy.ts.cn/news/node_1075": '100',
        "http://uy.ts.cn/news/node_14742": '100',
        "http://uy.ts.cn/node_964": '50',
        "http://uy.ts.cn/news/node_904": '100',
        "http://uy.ts.cn/news/node_905": '100',
        "http://uy.ts.cn/life/index": '98',
        "http://uy.ts.cn/wenxue/node_922": '45',
        "http://uy.ts.cn/wenxue/node_926": '68',
        "http://uy.ts.cn/wenxue/node_924": '23',
        "http://uy.ts.cn/xinjiang/node_913": '56',
        "http://uy.ts.cn/xinjiang/node_914": '15'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.f_link = open(self.link_file, 'w', encoding='utf-8')
        self.f_title = open(self.title_file, 'w', encoding='utf-8')

    def parse(self, response):
        self.list_arse(response)

    def list_arse(self, response):
        base_url = get_base_url(response)
        selector = Selector(response)
        titles = selector.xpath("//div[@class='layout']/div[@id='item_list']/a/em/text()").extract()
        for title in titles:
            print(title)
            self.f_title.write(title + '\n')

        urls = selector.xpath("//div[@class='layout']/div[@id='item_list']/a/@href").extract()
        for url in urls:
            full_url = response.urljoin(url)
            print(full_url)
            self.f_link.write(full_url + '\n')

    def closed(self, reason):
        self.f_link.close()
        self.f_title.close()