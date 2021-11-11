import scrapy


class CremeSpider(scrapy.Spider):
    name = 'creme'
    allowed_domains = ['emag.ro']
    start_urls = ['http://emag.ro/']

    def parse(self, response):
             for creme in response.css('div.card-item.card-standard.js-product-data'):
                 yield {
                     'descriere': creme.css('a.card-v2-title::text').get(),
                     'pret': creme.css('p.product-new-price::text').get(), 
                     'link': creme.css('a.card-v2-title').attrib['href']
                 }
             for page_nr in range(0,106):
              next_page = f'https://www.emag.ro/creme-fata/p{page_nr}/c'
              if next_page is not None:
                  yield response.follow(next_page, callback=self.parse)
