"""------=--=-=-=-=-=-=-=-=-------"""

stand_alone_scrips folder
-method 1 using:

put_data_in_mysql.py

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
 
 
 -method 2 using:
 put_data_in_mysql_using_pandas.py

--- more easy using pandas and sqlalchemy because there is no need to manualy create table columns content
--- there is just one step, to login into mysql docker container and create a database with the name: test_3 in this case, also edit the script column_names to match your file.cvs column names , you can the run the script
--- enjoy


  
"""------=--=-=-=-=-=-=-=-=-------"""
- use emag_laptopuri.py to scrape data, a file named emag_laptopuri.csv will be made
- use emag_placi_video.csv to scrape data, a file named emag_placi_vide.csv vill be created