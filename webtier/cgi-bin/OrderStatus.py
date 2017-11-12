#!/usr/bin/env python

# enable debugging
import cgitb
cgitb.enable()
import cgi

from Db.OrderStatus import OrderStatus
from Db.OrderStatusSearch import OrderStatusSearch

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

    orderStatus = OrderStatus(iId, '', '')
    orderStatus.load()

    print "Content-Type: application/json\r\n\r\n"
    print orderStatus.toJson('data', False, True)

elif sAction == "create" or sAction == "edit":
    orderStatus = OrderStatus(iId, sDescription, sStatus)
    orderStatus.save()

    print "Content-Type: application/json\r\n\r\n"
    print orderStatus.toJson('data', True, True)

elif sAction == "remove":
    orderStatus = OrderStatus(iId, '', '')
    orderStatus.delete()

    print "Content-Type: application/json\r\n\r\n"
    print '{ "data" : [ ]}'

elif sAction == "search":
    sStatus = form.getvalue('status')
    orderStatusSearch = OrderStatusSearch(sStatus)
    orderStatusSearch.search()

    print "Content-Type: application/json\r\n\r\n"
    print orderStatusSearch.toJson()

else:
    print "Content-Type: text/plain\r\n\r\n"
    print "Invalid action: " + sAction





