import scrapy


class LaptopSpider(scrapy.Spider):
    name = "laptop_lk"
    start_urls = [
        'https://www.laptop.lk/index.php/product-category/computers-accessories/laptops-tabs/commercial-notebooks/',
    ]

    def parse(self, response):
        for laptop in response.css('li.product.type-product'):
            yield {
                'name': laptop.css('h2.woocommerce-loop-product__title::text').get(),
                'price': laptop.css('span.electro-price>ins>span.woocommerce-Price-amount.amount>bdi>span.woocommerce-Price-currencySymbol::text').get() + ' ' + laptop.css('span.electro-price>ins>span.woocommerce-Price-amount.amount>bdi::text').get(),
                'link': laptop.css('a.woocommerce-LoopProduct-link.woocommerce-loop-product__link').attrib['href']
            }

        next_page = response.css('a.next.page-numbers').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            