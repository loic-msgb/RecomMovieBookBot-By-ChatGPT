import scrapy


class MoviespiderSpider(scrapy.Spider):
    name = "moviespider"
    allowed_domains = ["www.senscritique.com"]
    start_urls = ["https://www.senscritique.com/films/tops/top111"]

    def parse(self, response):
        moovies =  response.css('[data-testid = "product-list-item"]')
        for moovie in moovies:
            yield {
                'title': moovie.css('[data-testid = "product-title"]::text').get(),
                'duration': moovie.css('[data-testid = "duration"]::text').get(),
                'synopsis': moovie.css('[data-testid = "synopsis"]::text').get()
            }