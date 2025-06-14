import scrapy
from scrapy.selector import Selector
from scrapy.utils.response import get_base_url
from scrapy.http import Request

class BagdaxSpider(scrapy.Spider):
    name = "bagdax"
    allowed_domains = ["bbs.bagdax.cn"]
    start_urls = [
        "http://bbs.bagdax.cn/forum-2-1.html",  # example start URL
    ]

    def parse(self, response):
        base_url = get_base_url(response)
        selector = Selector(response)
        links = selector.xpath("//td/h2/a/@href").extract()
        for link in links:
            link = response.urljoin(link)
            yield Request(link, callback=self.parse_forum_list)

    def parse_forum_list(self, response):
        selector = Selector(response)
        last_page = selector.xpath("//span[@id = 'fd_page_bottom']/div/label/span/@title").extract()
        page = last_page[0].split(' ')[1] if last_page else '1'
        dot = response.url.split('-')
        line = dot[2].split('.')
        for i in range(1, int(page) + 1):
            url = f"{dot[0]}-{dot[1]}-{i}.{line[1]}"
            yield Request(url, callback=self.parse_list_content)

    def parse_list_content(self, response):
        # Implement your logic here for parsing list content
        pass