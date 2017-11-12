#!/usr/bin/env python

# enable debugging
import cgitb
cgitb.enable()
import cgi

from Db.CustomerType import CustomerType
from Db.CustomerTypeSearch import CustomerTypeSearch

#print "Content-Type: text/plain\r\n\r\n"

# Gather url paramters
form = cgi.FieldStorage()
sAction = form.getvalue('action')

if sAction == 'create' or sAction == 'edit' or sAction == 'remove':
    sId = form.keys()[1][5:form.keys()[1].find('][')]
    iId = int(sId)
    sDescription = str(form.getvalue('data['+sId+'][description]'))
    sStatus = str(form.getvalue('data['+sId+'][status]'))

if sAction == 'get':
    iId = str(form.getvalue("id"))

if sAction == None:
    print "Content-Type: text/plain\r\n\r\n"
    print "Missing action parameter.  Valid values are get, create, edit, and remove"

elif sAction == "get":

    customerType = CustomerType(iId, '', '')
    customerType.load()

    print "Content-Type: application/json\r\n\r\n"
    print customerType.toJson('data', False, True)

elif sAction == "create" or sAction == "edit":
    customerType = CustomerType(iId, sDescription, sStatus)
    customerType.save()

    print "Content-Type: application/json\r\n\r\n"
    print customerType.toJson('data', True, True)

elif sAction == "remove":
    customerType = CustomerType(iId, '', '')
    customerType.delete()

    print "Content-Type: application/json\r\n\r\n"
    print '{ "data" : [ ]}'

elif sAction == "search":
    sStatus = form.getvalue('status')
    customerTypeSearch = CustomerTypeSearch(sStatus)
    customerTypeSearch.search()

    print "Content-Type: application/json\r\n\r\n"
    print customerTypeSearch.toJson()

else:
    print "Content-Type: text/plain\r\n\r\n"
    print "Invalid action: " + sAction





