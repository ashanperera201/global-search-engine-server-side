import scrapy


class PatPatSpider(scrapy.Spider):
    name = "patpat"
    start_urls = [
        "https://www.patpat.lk/search?_token=hpSeRS42qxKgaGfSDvZ7VNzfQyLxfcdzggDFokty&search_txt=axio&category=vehicle",
    ]

    def __init__(self, category=None, *args, **kwargs):
        super(PatPatSpider, self).__init__(*args, **kwargs)
        # self.start_urls = [f'https://riyasewana.com/search/{category}']
        self.start_urls = [f'https://www.patpat.lk/search?_token=hpSeRS42qxKgaGfSDvZ7VNzfQyLxfcdzggDFokty&search_txt={category}&category=vehicle']

    def parse(self, response):
        for vehicle in response.css("div.result-item.col-10.col-sm-6.col-md-5.col-lg-12.mb-3"):
            yield {
                "name": vehicle.css("h4.result-title.mb-1>span::text").get(),
                "price": vehicle.css("h3.clearfix.my-1>label.w-100::text").get(),
                "link": vehicle.css("div.col-12.d-none.d-lg-block>a.mb-1").attrib["href"],
                "image" : vehicle.css('div.result-img.col-lg-3.px-lg-0>a>img').attrib['src'],
                "label" : "Patpat"
            }

        next_page_atr = response.css('li.page-item>a[rel="next"]')
        if len(next_page_atr) > 0:
            next_page = response.css('li.page-item>a[rel="next"]').attrib["href"]
            yield response.follow(next_page, callback=self.parse)