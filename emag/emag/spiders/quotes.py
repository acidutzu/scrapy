import scrapy


class QuotesSpider(scrapy.Spider):
 name = 'quotes'
 allowed_domains = ['quotes.toscrape.com']
 start_urls = ['http://quotes.toscrape.com/'] 
 
 
 def parse(self, response):
     for quote in response.css('div.quote'):
         yield {
             'quote': quote.css('span.text::text').get(),
             'author': quote.css('small.author::text').get(), 
         }
     for page_nr in range(0,10):
      next_page = f'http://quotes.toscrape.com/page/{page_nr}/'
      if next_page is not None:
          yield response.follow(next_page, callback=self.parse)
