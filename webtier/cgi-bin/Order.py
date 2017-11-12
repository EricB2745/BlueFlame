#!/usr/bin/env python

# enable debugging
import cgitb
cgitb.enable()
import cgi

from Db.Order import Order
from Db.OrderSearch import OrderSearch

#print "Content-Type: text/plain\r\n\r\n"

# Gather url paramters
form = cgi.FieldStorage()
sAction = form.getvalue('action')

if sAction == 'create' or sAction == 'edit' or sAction == 'remove':
    sId = form.keys()[1][5:form.keys()[1].find('][')]
    iId = int(sId)
    sName = str(form.getvalue('data['+sId+'][name]'))
    iCustTypeId = form.getvalue('data['+sId+'][custtypeid]')
    sPriority = str(form.getvalue('data[' + sId + '][priority]'))

if sAction == 'get':
    iId = str(form.getvalue("id"))

if sAction == None:
    print "Content-Type: text/plain\r\n\r\n"
    print "Missing action parameter.  Valid values are get, create, edit, and remove"

elif sAction == "get":

    order = Order(iId, '', '', '', '', '', '')
    order.load()

    print "Content-Type: application/json\r\n\r\n"
    print order.toJson('data', False, True)

elif sAction == "create" or sAction == "edit":
    order = Order(iId, sName, iCustTypeId, sPriority)
    order.save()

    print "Content-Type: application/json\r\n\r\n"
    print order.toJson('data', True, True)

elif sAction == "remove":
    order = Order(iId, '', '', '', '', '', '')
    order.delete()

    print "Content-Type: application/json\r\n\r\n"
    print '{ "data" : [ ]}'

elif sAction == "search":
    sStatus = form.getvalue('status')
    orderSearch = OrderSearch(sStatus)
    orderSearch.search()
    custJson = orderSearch.toJson()

    # insert options clause and closing brace
    returnJson = custJson

    print "Content-Type: application/json\r\n\r\n"
    print returnJson

else:
    print "Content-Type: text/plain\r\n\r\n"
    print "Invalid action: " + sAction





