#!/usr/bin/env python

# enable debugging
import cgitb
cgitb.enable()
import cgi

# Gather url paramters
form = cgi.FieldStorage()

print "Content-Type: text/plain\r\n\r\n"

for key in form.keys():
    print key + ":" + form.getvalue(key)

sId = form.keys()[1][5:form.keys()[1].find('][')]
iId = int(sId)
sDescription = form.getvalue('data[' + sId + '][description]')
sStatus = form.getvalue('data[' + sId + '][status]')

print str(sId)
print str(sDescription)
print str(sStatus)



if sAction == None:
    print "Content-Type: text/plain\r\n\r\n"
    print "Missing action parameter.  Valid values are get, create, edit, and remove"

elif sAction == "get":

    orderStatus = OrderStatus(iId, '', '')
    orderStatus.load()

    print "Content-Type: application/json\r\n\r\n"
    print orderStatus.toJson()

elif sAction == "create":
    orderStatus = OrderStatus(iId, sDescription, sStatus)
    orderStatus.save()

    print "Content-Type: application/json\r\n\r\n"
    print orderStatus.toJson()

elif sAction == "edit":
    orderStatus = OrderStatus(iId, sDescription, sStatus)
    orderStatus.save()

    print "Content-Type: application/json\r\n\r\n"
    print orderStatus.toJson()

elif sAction == "remove":
    orderStatus = OrderStatus(iId, '', '')
    orderStatus.delete()

    print "Content-Type: text/plain\r\n\r\n"
    print "Order Status with id " + str(iId) + " was deleted successfully"

elif sAction == "search":
    sStatus = form.getvalue('status')
    orderStatusSearch = OrderStatusSearch(sStatus)
    orderStatusSearch.search()

    print "Content-Type: application/json\r\n\r\n"
    print orderStatusSearch.toJson()

else:
    print "Content-Type: text/plain\r\n\r\n"
    print "Invalid action: " + sAction