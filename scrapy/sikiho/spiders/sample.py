import scrapy


class SampleSpider(scrapy.Spider):
    name = "shikiho.toyokeizai"
    allowed_domains = ["shikiho.toyokeizai.net"]
    start_urls = ["http://shikiho.toyokeizai.net/"]

    def parse(self, response):
        # タイトルを抽出して表示
        title = response.xpath("//title/text()").get()
        print(f"Page title: {title}")

        # 他のページへのリンクを取得し、再帰的にたどる
        for href in response.xpath("//a/@href").extract():
            url = response.urljoin(href)
            yield scrapy.Request(url, self.parse)
