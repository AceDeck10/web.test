#!/usr/bin/env python3

print('Content-Type: text/html\n')

import cgi

form = cgi.FieldStorage()

name = form.getvalue('name')
passwd = form.getvalue('password')

print(name)
print(passwd)
