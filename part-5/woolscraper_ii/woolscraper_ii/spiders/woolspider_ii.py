import scrapy


class WoolspiderIiSpider(scrapy.Spider):
    name = "woolspider_ii"
    allowed_domains = ["woolwarehouse.co.uk"]
    start_urls = ["https://www.woolwarehouse.co.uk/yarn"]

    def parse(self, response):
        yarns = response.css('li.item')

        for yarn in yarns:
            next_page = yarn.css('h2 a ::attr(href)').get()

            yield response.follow(next_page, callback=self.parse)


        # yield{
        #         'name': yarn.css('h2 a::text').get(),
        #         'price': yarn.css('.gbp-price .gbp-price-value ::text').get(),
        #         'url': yarn.css('h2 a').attrib['href']
        #     }