import scrapy


class BaiduSpider(scrapy.Spider):  # 爬取该网页的爬虫的名字，用于运行爬虫时，使用的值
    name = "baidu"  # 允许访问的域名
    allowed_domains = ["www.baidu.com"] # 起始的URL地址，指的是“第一次”访问的域名
    start_urls = ["https://www.baidu.com"]  #start urIs 是在allowed_domains的前面添加一个    http://   ，在 allowed domains的后面添加一个 /

    def parse(self, response):  #是执行了start_urls之后执行的方法，方法中的response就是返回的那个对象，相当于 response = urllib.request.urlopen()或者response = requests.get()
        pass
