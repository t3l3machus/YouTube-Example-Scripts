'''
Author: Panagiotis Chartas (t3l3machus)
Video: https://youtu.be/dQgWvAQmZFI

--------------------------( Requirements )------------------------------
	
 pip install SQLAlchemy, psycopg2


--------------------------( Test Queries )------------------------------

1) Create table

CREATE TABLE Users (
   _id serial PRIMARY KEY,                  #auto-increment column
   username VARCHAR(20) UNIQUE NOT NULL,
   password VARCHAR(32) NOT NULL,
   postcode INTEGER
);

# One liner:
CREATE TABLE Users (_id serial PRIMARY KEY, username VARCHAR(20) UNIQUE NOT NULL, password VARCHAR(32) NOT NULL, postcode INTEGER);	



2) Write data in table

INSERT INTO Users(username, password, postcode) VALUES ('t3l3machus', 'PleaseSubscribe', 99999);
	
'''

import sqlalchemy # Object-Relational Mapper (ORM) = Bridge object-oriented programs with relational databases
import psycopg2 # Python interface to interact with PostgreSQL databases

# Connect to a database "testdb" as user "testuser"
# Edit the url to match your DB setup
url = "postgresql://testuser:12345@127.0.0.1:5432/testdb"
engine = sqlalchemy.create_engine(url)

try:
	engine.connect()
	print('[*] Database server connection established!\n')

except Exception as e:
	print(f'[X] Database server connection failed: {e}')
	

# Start SQL shell
while True:
	
	query = input('SQL: ') # Instead of input, you can create predefined queries (strings) that you want your program to run against the DB
	
	if query.strip():
		
		try:
			result = engine.execute(query)
			print(result.fetchall())
			
		except sqlalchemy.exc.ResourceClosedError: 
			# Silently moves on when queries do not return data
			continue
			
		except Exception as e:
			print(f'Something went wrong: {e}')
			
	else:
		continue
