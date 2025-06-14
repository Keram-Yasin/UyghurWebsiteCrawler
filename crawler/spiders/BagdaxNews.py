import scrapy

class BagdaxNewsSpider(scrapy.Spider):
    name = "bagdaxnews"
    start_urls = []
    file_name = "bagdaxnews.txt"

    urls = {
        "http://world.bagdax.cn/": '340',
        "http://cn.bagdax.cn/": '43',
        "http://xj.bagdax.cn/": '34',
        "http://finance.bagdax.cn/": '8',
        "http://special.bagdax.cn/": '1',
        "http://entrepreneur.bagdax.cn/": '2',
        "http://enterprise.bagdax.cn/": '3',
        "http://study-abroad.bagdax.cn/": '1',
        "http://wiki.bagdax.cn/": '1',
        "http://sports.bagdax.cn/": '19',
        "http://mixed.bagdax.cn/": '20'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.f_file = open(self.file_name, 'w', encoding='utf-8')

    def closed(self, reason):
        self.f_file.close()