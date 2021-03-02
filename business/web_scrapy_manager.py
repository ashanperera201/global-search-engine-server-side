import scrapy


class WebScraper(scrapy.Spider):
    name = "cars"
    start_urls = [
        "https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock",
    ]

    def parse(self, response):
        for products in response.css("div.product-item-info"):
            try:
                yield {
                    "name": products.css("a.product-item-link::text").get(),
                    "price": products.css("span.price::text").get(),
                    "link": products.css("a.product-item-link").attrib["href"],
                }
            except:
                yield {
                    "name": products.css("a.product-item-link::text").get(),
                    "price": "Sold out",
                    "link": products.css("a.product-item-link").attrib["href"],
                }
        next_page = response.css("a.action.next").attrib["href"]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
