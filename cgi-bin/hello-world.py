#!/usr/bin/env python3
print("Status: 302")
print("Location: ./index.html?msg=executed")
print('Content-Type: text/html\n')

DB_HOST = 'localhost'
DB_NAME = 'webtest_db'
DB_USER = 'postgres'
DB_PASS = '@c3c0m10'

import cgi
import psycopg2

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)




form = cgi.FieldStorage()

name = form.getvalue('name')
passwd = form.getvalue('password')


cur = conn.cursor()

cur.execute('INSERT INTO Users(username, user_passwd) VALUES(' + name + ',' + passwd + ')')

print()
print(name)
print(passwd)

cur.close()
