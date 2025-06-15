import scrapy

class HackerNewsSpider(scrapy.Spider):
    name = "hackernews"
    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):
        # loop through news entries
        for post in response.css('tr.athing'):
            title = post.css('span.titleline a::text').get()
            link = post.css('span.titleline a::attr(href)').get()

            # Only follow valid HTTP/HTTPS links
            if link and link.startswith(('http', 'https')):
                yield response.follow(link, callback=self.parse_article, meta={'title': title})

    def parse_article(self, response):
        title = response.meta['title']

        # Try to extract visible text content from body
        paragraphs = response.css('p::text').getall()
        content = ' '.join(paragraphs).strip()

        # Fallback if no <p> tags
        if not content:
            content = ' '.join(response.css('body ::text').getall()).strip()

        yield {
            'title': title,
            'content': content[:1000]  # Limit content for readability
        }

