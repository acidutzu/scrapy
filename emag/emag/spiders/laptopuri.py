import scrapy


class LaptopuriSpider(scrapy.Spider):
    name = 'laptopuri'
    allowed_domains = ['emag.ro']
    start_urls = ['http://emag.ro/']

    def parse(self, response):
         for laptop in response.css('div.card-item.card-standard.js-product-data'):
             yield {
                 'pret': laptop.css('p.product-new-price::text').get().replace('.',''),
                 'descriere': laptop.css('a.card-v2-title::text').get(),
                 'link': laptop.css('a.card-v2-title').attrib['href'],
                 #'link': laptop.css('a.card-v2-title::attr(href)')
             }
         for page_nr in range(0,3):
          next_page = f'/laptopuri/p{page_nr}/c'
          if next_page is not None:
              yield response.follow(next_page, callback=self.parse)