import scrapy


class RiyasewanaSpider(scrapy.Spider):
    name = "riyasewana_com"
    start_urls = [
        'https://riyasewana.com/search/corolla',
    ]

    def parse(self, response):
        for riyasewana in response.css('li.item.round'):
            yield {
                'name': riyasewana.css('h2.more>a::text').get(),
                'price': riyasewana.css('div.boxtext>div.boxintxt.b::text').get(),
                'link': riyasewana.css('h2.more>a').attrib['href'],
                'image': 'https:' + riyasewana.css('div.imgbox>a>img').attrib['src']
            }

        # next_page_atr = response.css('li>a[rel="next"]')
        # next_page_atr = response.css('div.pagination::a[text=Next]')
        next_page_atr = response.xpath("//a[contains(.//text(), 'Next')]").getall()
        if len(next_page_atr) > 0:
            next_page = response.xpath("//a[contains(.//text(), 'Next')]").attrib['href']
            next_page = 'https:' + next_page
            yield response.follow(next_page, callback=self.parse)
# scrapy crawl riyasewana_com