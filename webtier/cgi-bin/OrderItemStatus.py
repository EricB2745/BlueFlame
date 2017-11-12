#!/usr/bin/env python

# enable debugging
import cgitb
cgitb.enable()
import cgi

from Db.OrderItemStatus import OrderItemStatus
from Db.OrderItemStatusSearch import OrderItemStatusSearch

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

    orderItemStatus = OrderItemStatus(iId, '', '')
    orderItemStatus.load()

    print "Content-Type: application/json\r\n\r\n"
    print orderItemStatus.toJson('data', False, True)

elif sAction == "create" or sAction == "edit":
    orderItemStatus = OrderItemStatus(iId, sDescription, sStatus)
    orderItemStatus.save()

    print "Content-Type: application/json\r\n\r\n"
    print orderItemStatus.toJson('data', True, True)

elif sAction == "remove":
    orderItemStatus = OrderItemStatus(iId, '', '')
    orderItemStatus.delete()

    print "Content-Type: application/json\r\n\r\n"
    print '{ "data" : [ ]}'

elif sAction == "search":
    sStatus = form.getvalue('status')
    orderItemStatusSearch = OrderItemStatusSearch(sStatus)
    orderItemStatusSearch.search()

    print "Content-Type: application/json\r\n\r\n"
    print orderItemStatusSearch.toJson()

else:
    print "Content-Type: text/plain\r\n\r\n"
    print "Invalid action: " + sAction





