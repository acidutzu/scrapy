"""
-make sure you are in a desired directory
-and in vscode terminal create a virtual env:                           virtualenv -p python3 venv ,
if you don't have virtualenv module installed you can install it by :   pip3 install virtualenv
-then activate the virtualenviroment that you created:                  source venv/bin/activate
-after that you may install scrapy into the virtual enviroment venv:    pip3 install scrapy
-then you can go ahead and start a project:                             scrapy startproject project-name
-make a new.py file inside your project, into the spiders folder,
  where all other files are, like this one here,  where you will write your code
---use scrapy shell to connect to a page and interogate it, 
test commands before making this code here:                             scrapy shell
---in scrapy shell use fetch command to fetch data from a url:          fetch('https://you.com')

fetch command will save everything in the command :                     response
use response.css or response.xpath

to start the crawler, be in venv, and inside project folder name: scrapy crawl name -O name.json
and if everything is ok you will find a file name.json containing scraped data

"""


import scrapy


class PaianganuOne(scrapy.Spider):
    name = "emag"
    page_number = 1
    start_urls = [
                'https://www.emag.ro/laptopuri/filter/tip-laptop-f7882,home-v-3292210/c?ref=subcat_1_fashion-grid_1'
               # 'https://blog.scrapinghub.com/page/2/' 
    ]

    def parse(self, response):
     for prod in response.css('div.card-item.card-standard'):
        yield {
            'pret': prod.css('p.product-new-price::text').get(),
            'produs': prod.css('a.card-v2-title::text').get(),
            'link': prod.css('a.card-v2-title').attrib['href'],
            
            
        }

        #next_page = response.css('a.js-change-page').attrib['href']
        next_page = 'https://www.emag.ro/laptopuri/filter/tip-laptop-f7882,home-v-3292210/p'+ str(PaianganuOne.page_number)+'/c'
        if PaianganuOne.page_number <=14:
            PaianganuOne.page_number += 1
        #if next_page is not None: 
            yield response.follow(next_page, callback=self.parse)