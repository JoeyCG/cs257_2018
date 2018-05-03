#!/usr/bin/env python3
'''
    psycopg2-sample.py
    Jeff Ondich, 23 April 2016

    A very short demo of how to use psycopg2 to connect to and
    query a PostgreSQL database. This demo assumes a "books"
    database like the one I've used in CS257 Spring 2016, including
    an authors table with fields (id, first_name, last_name,...).

    You might also want to consult the official psycopg2 tutorial
    at https://wiki.postgresql.org/wiki/Psycopg2_Tutorial.
'''
import psycopg2

# Storing your user name and password directly in your code
# is easiest:
#
#   database = 'yourdatabasename'
#   user = 'yourusername'
#   password = 'yourdatabasepassword'
#
# However, this introduces potential security problems, which we'll
# discuss in class. One common mitigation of these dangers is to put
# the data in a separate module that's in the Python import path,
# but not in the web server's file tree.
from config import password
from config import database
from config import user

# Login to the database
try:
    connection = psycopg2.connect(database=database, user=user, password=password)
except Exception as e:
    print(e)
    exit()

# Query the database, leaving you with a "cursor"--an object you can
# use to iterate over the rows generated by your query.
try:
    cursor = connection.cursor()
    query = 'SELECT first_name, last_name FROM authors ORDER BY last_name'
    cursor.execute(query)
except Exception as e:
    print(e)
    exit()

# We have a cursor now. Iterate over its rows to print the results.
print('===== All authors =====')
for row in cursor:
    print(row[0], row[1])
print()

# Do you have parameters to put into your query? To avoid
# the very common and very dangerous security attack known
# as "SQL Injection", use the parameterized version of
# cursor.execute, like so.
search_string = 'Brontë'
query = '''SELECT first_name, last_name
           FROM authors
           WHERE last_name = %s'''
try:
    cursor.execute(query, (search_string,))
except Exception as e:
    print(e)
    exit()

print('===== Authors with last name {0} ====='.format(search_string))
for row in cursor:
    print(row[0], row[1])
print()

# Don't forget to close the database connection.
connection.close()

