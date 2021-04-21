import scrapy


class Spider(scrapy.Spider):
    name = "www.patpat.lk"
    start_urls = [
        "https://www.patpat.lk/search?_token=hpSeRS42qxKgaGfSDvZ7VNzfQyLxfcdzggDFokty&search_txt=axio&category=vehicle",
    ]

    def parse(self, response):
        for vehicle in response.css("li.breadcrumb-item"):
            yield {
                "name": vehicle.css("h4.result-title.no-dt.mb-2>a::text").get(),
                "price": vehicle.css("h3.clearfix.my-1::text").get(),
                "link": vehicle.css("div.mb-1.d-lg-none>a").attrib["href"],
            }

        next_page_atr = response.css("li.pagination.pagiination.page-item-next")
        if len(next_page_atr) > 0:
            next_page = response.css("a.action.next").attrib["href"]
            yield response.follow(next_page, callback=self.parse)