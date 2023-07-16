import scrapy


class PolskiDailySpider(scrapy.Spider):
    name = "polski_daily"
    allowed_domains = ["www.polskidaily.eu"]
    start_urls = ["https://www.polskidaily.eu/course/"]

    def parse(self, response):
        podcasts = response.css('div.podcast-content')

        for podcast in podcasts:
            textContent = podcast.css('//h2/a/text()').get()
            episode, title = textContent.split(max_split=1)

            data = {
                'episode': episode,
                'title': title,
                'url': podcast.xpath('//h2/a').attrib['href']
            }

            yield data