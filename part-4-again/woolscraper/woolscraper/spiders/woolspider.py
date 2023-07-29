import scrapy


class WoolspiderSpider(scrapy.Spider):
    name = "woolspider"
    allowed_domains = ["www.woolwarehouse.co.uk/yarn"]
    start_urls = ["https://www.woolwarehouse.co.uk/yarn"]

    def parse(self, response):
        yarns = response.css('li.item')

        for yarn in yarns:
            yield{
                'name': yarn.css('h2 a::text').get(),
                'price': yarn.css('.gbp-price .gbp-price-value ::text').get(),
                'url': yarn.css('h2 a').attrib['href']
            }

        next_page = response.css('.changepagebutton ::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)