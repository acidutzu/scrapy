import scrapy


class PrezervativeSpider(scrapy.Spider):
    name = 'prezervative'
    allowed_domains = ['emag.ro']
    start_urls = ['http://emag.ro/']

    def parse(self, response):
         for prez in response.css('div.card-item.card-standard.js-product-data'):
             yield {
                 'descriere': prez.css('a.card-v2-title::text').get(),
                 'pret': prez.css('p.product-new-price::text').get(), 
                 'link': prez.css('a.card-v2-title').attrib['href']
             }
         for page_nr in range(0,10):
          next_page = f'https://www.emag.ro/prezervative/p{page_nr}/c'
          if next_page is not None:
              yield response.follow(next_page, callback=self.parse)