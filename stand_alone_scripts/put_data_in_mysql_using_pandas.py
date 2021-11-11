import pandas as pd
from sqlalchemy import create_engine

# Credentials to database connection
hostname="192.168.1.131"
dbname="test_3"
uname="root"
pwd="parola"

# read CSV file content
column_names = ['pret','descriere', 'link']

df = pd.read_csv('emag_placi_video.csv', header = None, names = column_names)
print(df)

df = pd.read_csv('emag_placi_video.csv', header = 0)
print(df)

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

# Convert dataframe to sql table 
df.to_sql('produse', engine, if_exists='append', index=False)
