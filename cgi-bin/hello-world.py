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
import requests

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

form = cgi.FieldStorage()

name = form.getvalue('name')
passwd = form.getvalue('password')


cur = conn.cursor()

cur.execute('INSERT INTO tbl_users(username, user_passwd) VALUES(%s, %s)', (name, passwd))
conn.commit()

cur.execute('SELECT * FROM tbl_users WHERE username=' + name)
allUsers = cur.fetchall()

#for row in allUsers:
#    print('Id = ', row[0])
#    print('Username = ', row[1])
#    print('Password = ', row[2])
#    print('<br/>')

res = requests.get('http://127.0.0.1:8000/index.html?name=' + name + 'Password=' + passwd)
res.content

cur.close()
