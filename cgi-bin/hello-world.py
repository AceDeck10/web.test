#!/usr/bin/env python3

DB_HOST = 'localhost'
DB_NAME = 'webtest_db'
DB_USER = 'postgres'
DB_PASS = '@c3c0m10'

import cgi
import http
import http.server
from urllib.parse import urlparse
from urllib.parse import parse_qs
import psycopg2
import requests

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        name = 'World'
        query_components = parse_qs(urlparse(self.path).query)
        if 'name' in query_components:
            name = query_components['name'][0]
        
        html = res.text
        self.wfile.write(bytes(html, 'utf8'))

        return

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

form = cgi.FieldStorage()

name = form.getvalue('name')
passwd = form.getvalue('password')


cur = conn.cursor()

cur.execute('INSERT INTO tbl_users(username, user_passwd) VALUES(%s, %s)', (name, passwd))
conn.commit()

cur.execute('SELECT * FROM tbl_users')
allUsers = cur.fetchall()

#for row in allUsers:
#    print('Id = ', row[0])
#    print('Username = ', row[1])
#    print('Password = ', row[2])
#    print('<br/>')

res = requests.get('http://127.0.0.1:8000/index.html?name=' + name + 'Password=' + passwd)
print(res.status_code)
print(res.history)
print(res.url)
print(res.text)


cur.close()
