import scrapy


class SaetSpider(scrapy.Spider):
    name = "24saet"
    allowed_domains = ["24saet.com"]
    start_urls = ["https://www.24saet.com/"]

    def parse(self, response):
        # Follow article links
        for article_link in response.css('a::attr(href)').getall():
            if article_link.startswith("https://www.24saet.com/") and "/news/" in article_link:
                yield response.follow(article_link, self.parse_article)

        # Follow pagination if needed
        next_page = response.css('a.page-link::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        yield {
            'url': response.url,
            'title': response.css('h1::text').get(),
            'date': response.css('div.post-date::text').get(),
            'content': ' '.join(response.css('div.post-content p::text').getall()).strip(),
        }

