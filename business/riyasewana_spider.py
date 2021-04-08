import scrapy


class RiyasewanaSpider(scrapy.Spider):
    name = "riyasewana_com"
    start_urls = [
        'https://riyasewana.com/search/civic-es8',
    ]

    def parse(self, response):
        for riyasewana in response.css('li.item.round'):
            yield {
                'name': riyasewana.css('h2.more>a::text').get(),
                'price': riyasewana.css('div.boxtext>div.boxintxt.b::text').get(),
                'link': riyasewana.css('h2.more>a').attrib['href']
            }

        next_page_atr = response.css('li>a[rel="next"]')
        next_page_atr = response.css('div.pagination::[text=Next]')
        if len(next_page_atr) > 0:
            next_page = response.css('div.pagination::[text=Next]').attrib['href']
            yield response.follow(next_page, callback=self.parse)
# scrapy crawl riyasewana_com