import scrapy
from scrapy.crawler import CrawlerProcess
import time

class Emag(scrapy.Spider):
    name = 'emag'

    def start_requests(self):
        yield scrapy.Request('https://www.emag.ro/sociologie-filozofie/sort-priceasc/c')


    def parse(self, response):
        produse = response.css('div.card-item.card-standard.js-product-data')
        for produs in produse:
            yield {
                 'pret': produs.css('p.product-new-price::text').get().replace('.',''),
                 'descriere': produs.css('a.card-v2-title::text').get(),
                 'link': produs.css('a.card-v2-title').attrib['href'],
            }
        #time.sleep(1.3)    
        for page_nr in range(0,189):
             yield scrapy.Request(f'https://www.emag.ro/sociologie-filozofie/sort-priceasc/p{page_nr}/c', callback=self.parse)              

process = CrawlerProcess(settings= {
    'FEED_URI': 'emag_carti_socio_filozofie.csv',
    'FEED_FORMAT':'csv',
    #'FEEDS': 'overwrite = True'
     })

process.crawl(Emag)
process.start()