import scrapy


class Nolimit(scrapy.Spider):
    name = "nolimit"
    start_urls = [
        'https://www.nolimit.lk/products?categories%5B%5D=&q=trouser',
    ]

    def parse(self, response):
        for laptop in response.css('div.row.shop_container.grid>div.col-md-4.col-6'):
            yield {
                'name': laptop.css('h6.product_title>a::text').get(),
                'price': laptop.css('div.product_price>span.price::text').get(),
                'link': laptop.css('h6.product_title>a').attrib['href']
            }

        next_page_atr = response.css('li.page-item>a.page-link[rel="next"]')
        if len(next_page_atr) > 0:
            next_page = response.css('li.page-item>a.page-link[rel="next"]').attrib['href']
            yield response.follow(next_page, callback=self.parse)
