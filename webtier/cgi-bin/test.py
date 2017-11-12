#!/usr/bin/env python

# enable debugging
import cgitb
cgitb.enable()
import cgi

print "Content-Type: text/plain\r\n\r\n"
print

print "Hello World!"

# url test.py?param1=hello&param2=7
form = cgi.FieldStorage()
param1 = form.getvalue('param1')
print param1

param2 = form.getvalue('param2')
print param2