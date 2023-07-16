import scrapy


class PolskiDailySpider(scrapy.Spider):
    name = "polski_daily"
    allowed_domains = ["www.polskidaily.eu"]
    start_urls = ["https://www.polskidaily.eu/podcasts-recourse/"]

    def parse(self, response):
        podcasts = response.xpath("/div[@class='podcast-content']")

        for podcast in podcasts:
            textContent = podcast.css('//h2/a/text()').get()
            episode, title = textContent.split(max_split=1)

            data = {
                'episode': episode,
                'title': title,
                'url': podcast.xpath('//h2/a').attrib['href']
            }

            yield data

        # go through all pages
        next_page_url = response.xpath("//ul[@class='page-numbers']//li//a[@class='next page-numbers']").attrib['href']
        if next_page_url is not None:
            print(next_page_url)
            yield response.follow(next_page_url, callback=self.parse)