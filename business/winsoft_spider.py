import scrapy


class WinsoftSpider(scrapy.Spider):
    name = "winsoft_lk"
    start_urls = [
        'https://winsoft.lk/catalogsearch/result//?q=asus',
        # 'https://winsoft.lk/catalog/category/view/s/dell/id/80/
    ]

    def parse(self, response):
        for laptop in response.css('li.item.product.product-item'):
            yield {
                'name': laptop.css('h2.product.name.product-name.product-item-name>a::text').get(),
                'price': laptop.css('span.price::text').get(),
                'link': laptop.css('h2.product.name.product-name.product-item-name>a').attrib['href']
            }

        next_page_atr = response.css('li.item.pages-item-next')
        if len(next_page_atr) > 0:
            next_page = response.css('a.action.next').attrib['href']
            yield response.follow(next_page, callback=self.parse)
