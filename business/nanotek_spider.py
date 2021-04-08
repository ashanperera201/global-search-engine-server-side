import scrapy


class NanotekSpider(scrapy.Spider):
    name = "nanotek_lk"
    start_urls = [
        'https://www.nanotek.lk/search?q=dell',
    ]

    def parse(self, response):
        for laptop in response.css('li.ty-catPage-productListItem'):
            yield {
                'name': laptop.css('div.ty-productBlock-title>h1::text').get(),
                'price': laptop.css('h2.ty-productBlock-price-retail::text').get(),
                'link': laptop.css('li.ty-catPage-productListItem>a').attrib['href']
            }

        next_page_atr = response.css('li>a[rel="next"]')
        if len(next_page_atr) > 0:
            next_page = response.css('li>a[rel="next"]').attrib['href']
            yield response.follow(next_page, callback=self.parse)
