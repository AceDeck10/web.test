#!/usr/bin/env python3
print("Status: 302")
print("Location: ./index.html?msg=executed")
print('Content-Type: text/html\n')

DB_HOST = ''
DB_NAME = ''
DB_USER = ''
DB_PASS = ''

import cgi

form = cgi.FieldStorage()

name = form.getvalue('name')
passwd = form.getvalue('password')

print()
print(name)
print(passwd)
