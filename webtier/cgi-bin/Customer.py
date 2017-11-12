#!/usr/bin/env python

# enable debugging
import cgitb
cgitb.enable()
import cgi

from Db.Customer import Customer
from Db.CustomerSearch import CustomerSearch
from Db.CustomerTypeSearch import CustomerTypeSearch

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

    customer = Customer(iId, '', '', '')
    customer.load()

    print "Content-Type: application/json\r\n\r\n"
    print customer.toJson('data', False, True)

elif sAction == "create" or sAction == "edit":
    customer = Customer(iId, sName, iCustTypeId, sPriority)
    customer.save()

    print "Content-Type: application/json\r\n\r\n"
    print customer.toJson('data', True, True)

elif sAction == "remove":
    customer = Customer(iId, '', '', '')
    customer.delete()

    print "Content-Type: application/json\r\n\r\n"
    print '{ "data" : [ ]}'

elif sAction == "search":
    sStatus = form.getvalue('status')
    customerSearch = CustomerSearch(sStatus)
    customerSearch.search()
    custJson = customerSearch.toJson()

    customerTypeSearch = CustomerTypeSearch("Active")
    customerTypeSearch.search()
    typeJson = customerTypeSearch.toJson()

    # turn all descriptions into label to make Json match options format
    typeJson = typeJson.replace('"description"', '"label"')
    typeJson = typeJson.replace('"id"', '"value"')
    typeJson = typeJson.replace('"CustomerTypes"', '"custtypeid"')

    # remove trailing brace
    custJson = custJson[:-1]

    # insert options clause and closing brace
    returnJson = custJson + ',  "options": ' + typeJson + '}'

    print "Content-Type: application/json\r\n\r\n"
    print returnJson

else:
    print "Content-Type: text/plain\r\n\r\n"
    print "Invalid action: " + sAction





