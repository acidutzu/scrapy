----------
stand_alone_scrips folder
tip: you cand find put_data_in_mysql.py script into folder stand_alone_scrips
----this script will connect to a MySQL database and import file emag_placi_video.csv
----the database has to be allready created before so for the script to work
----so here are basic SQL commands to create a database and a table:
 mysql basic commands
 
 create database test;

 show databases;

 use database test;

  create table `produse` (
    `pret` int(11) NOT NULL,
    `descriere` varchar(50) NOT NULL,
    `link` varchar(355) NOT NULL
    );

 #view content of the table produse
   
 desc produse;

  
"""------=--=-=-=-=-=-=-=-=-=-=-=-==-=-"""

emag folder:
how to use:

to start the crawler, first activate virtual env "venv" from emag folder : source venv/bin/activate

and inside project emag/emag/$

--- use : scrapy crawl emag -O name.csv

and if everything is ok you will find a file name.csv containing scraped data:
you can view the scraped data here: https://github.com/acidutzu/scrapy/blob/master/emag/emag/emag.csv

if you wanna start a new project then follow the intrusctions bellow:

-make sure you are in a desired directory

-and in vscode terminal create a virtual env: virtualenv -p python3 venv ,

if you don't have virtualenv module installed you can install it by : pip3 install virtualenv

-then activate the virtualenviroment that you created: source venv/bin/activate

-after that you may install scrapy into the virtual enviroment venv: pip3 install scrapy

-then you can go ahead and start a project: scrapy startproject project-name

-make a new.py file inside your project, into the spiders folder, where all other files are, like this one here, where you will write your code

---use scrapy shell to connect to a page and interogate it, test commands before making this code here: scrapy shell

---in scrapy shell use fetch command to fetch data from a url: fetch('https://site.com')

fetch command will save everything in the command : response

use response.css or response.xpath

"""

webscraping projects

