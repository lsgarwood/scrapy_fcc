import scrapy


class WoolspiderIiSpider(scrapy.Spider):
    name = "woolspider_ii"
    allowed_domains = ["woolwarehouse.co.uk"]
    start_urls = ["https://www.woolwarehouse.co.uk/yarn"]

    def parse(self, response):
        yarns = response.css('li.item')

        for yarn in yarns:
            yarn_url = yarn.css('h2 a ::attr(href)').get()

            yield response.follow(yarn_url, callback=self.parse_book_page)

    def parse_book_page(self, response):
        pass


        # yield{
        #         'name': yarn.css('h2 a::text').get(),
        #         'price': yarn.css('.gbp-price .gbp-price-value ::text').get(),
        #         'url': yarn.css('h2 a').attrib['href']
        #     }

        # hxs = HtmlXPathSelector(response)
        # items = hxs.select('//table[@class="tablehd"]/td')

        # for item in items:
        #     my_item = MyItem()
        #     my_item['value'] = item.select('.//text()').extract()
        #     yield my_item

        # response.css('.data-table ::text').getall()