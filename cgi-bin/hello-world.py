#!/usr/bin/env python3

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

cur.execute('INSERT INTO tbl_users(username, user_passwd) VALUES(%s, %s)', (name, passwd))
conn.commit()

cur.execute('SELECT * FROM tbl_users')
allUsers = cur.fetchall()
cur.close()

print("Status: 303\r\n")
print("Location: http://127.0.0.1:8000/index.html/\r\n")
print("Content-Type: text/html\r\n")
#print("Location: http://127.0.0.1:8000/index.html?name=" + name + "&Password=" + passwd"/r/n")