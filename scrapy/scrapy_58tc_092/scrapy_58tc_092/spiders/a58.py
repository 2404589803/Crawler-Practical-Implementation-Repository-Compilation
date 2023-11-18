import scrapy


class A58Spider(scrapy.Spider):
    name = "58"
    allowed_domains = ["cn.58.com"]
    start_urls = ["https://cn.58.com/"]

    def parse(self, response):
        pass
