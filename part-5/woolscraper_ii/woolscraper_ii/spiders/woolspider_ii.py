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

        next_page = response.css('.changepagebutton ::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_book_page(self, response):
        table_rows = response.css("table tr")

        yield {
            'brand_name': table_rows[0].css("td ::text").get(),
            'yarn_name': table_rows[1].css("td ::text").get(),
            'man_part_code': table_rows[2].css("td ::text").get(),
            # 'shade': hi,
            # 'ball_weight': hi,
            # 'length': hi,
            # 'needle_size': hi,
            # 'blend': hi,
            # 'url': response.url
        }