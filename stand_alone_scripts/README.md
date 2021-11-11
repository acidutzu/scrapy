"""------=--=-=-=-=-=-=-=-=-------"""

stand_alone_scrips folder

tip: you cand find put_data_in_mysql.py script into folder stand_alone_scrips

----this script will connect to a MySQL database and import file emag_placi_video.csv

----the database has to be allready created before so for the script to work

----so here are basic SQL commands to create a database and a table:

----connect to docker container tha runs MySQL:

sudo docker exec -it mysql mysql -p

here are some mysql basic commands:
 
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

  
"""------=--=-=-=-=-=-=-=-=-------"""