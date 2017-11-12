#!/usr/bin/env python

# enable debugging
import cgitb
cgitb.enable()
import cgi

from Db.OrderItem import OrderItem
from Db.OrderItemSearchByOrderId import OrderItemSearchByOrderId

#print "Content-Type: text/plain\r\n\r\n"

# Gather url paramters
form = cgi.FieldStorage()
sAction = form.getvalue('action')

if sAction == 'add' or sAction == 'modify' or sAction == 'delete':  #simple add from get

    iId = int(form.getvalue('id'))
    iOrderId = int(form.getvalue('orderid'))
    iOrderItemStatusId = form.getvalue('orderitemstatusid')
    iColorId = form.getvalue('carttypeid')
    iCartTypeId = form.getvalue('colorid')
    iQuantity = form.getvalue('quantity')
    sDescription = form.getvalue('description')
    sSpecialInstructions = form.getvalue('specialinstructions')
    iQtyOfCarts = form.getvalue('qtyofcarts')
    sOverSize = form.getvalue('oversize')
    sPriority = form.getvalue('priority')
    sRequiresMasking = form.getvalue('requriesmaskorplug')
    sRequiresSandblasting = form.getvalue('requiressandblasting')
    fPricePer = form.getvalue('priceper')
    dCreateDate = form.getvalue('createdate')
    fSubTotal = form.getvalue('subtotal')


if sAction == 'create' or sAction == 'edit' or sAction == 'remove':
    sId = form.keys()[1][5:form.keys()[1].find('][')]
    iId = int(sId)

    iOrderId = form.getvalue('data['+sId+'][orderid]')
    iOrderItemStatusId = form.getvalue('data['+sId+'][orderitemstatusid]')
    iColorId = form.getvalue('data['+sId+'][carttypeid]')
    iCartTypeId = form.getvalue('data['+sId+'][colorid]')
    iQuantity = form.getvalue('data['+sId+'][quantity]')
    sDescription = str(form.getvalue('data['+sId+'][description]'))
    sSpecialInstructions = str(form.getvalue('data['+sId+'][specialinstructions]'))
    iQtyOfCarts = form.getvalue('data['+sId+'][qtyofcarts]')
    sOverSize = str(form.getvalue('data['+sId+'][oversize]'))
    sPriority = str(form.getvalue('data['+sId+'][priority]'))
    sRequiresMasking = str(form.getvalue('data['+sId+'][requriesmaskorplug]'))
    sRequiresSandblasting = str(form.getvalue('data['+sId+'][requiressandblasting]'))
    fPricePer = form.getvalue('data['+sId+'][priceper]')
    dCreateDate = form.getvalue('data['+sId+'][createdate]')
    fSubTotal = form.getvalue('data['+sId+'][subtotal]')



if sAction == 'get':
    iId = str(form.getvalue("id"))

if sAction == None:
    print "Content-Type: text/plain\r\n\r\n"
    print "Missing action parameter.  Valid values are get, create, edit, and remove"

elif sAction == "get":

    orderItem = OrderItem(iId, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    orderItem.load()

    print "Content-Type: application/json\r\n\r\n"
    print orderItem.toJson('data', False, True)

elif sAction == "create" or sAction == "edit" or sAction=="add" or sAction == "modify":
    orderItem = OrderItem(iId, iOrderId,iOrderItemStatusId,iColorId,iCartTypeId,iQuantity,sDescription,sSpecialInstructions,iQtyOfCarts,sOverSize,
                          sPriority,sRequiresMasking,sRequiresSandblasting,fPricePer,dCreateDate,fSubTotal)
    orderItem.save()

    print "Content-Type: application/json\r\n\r\n"
    print orderItem.toJson('data', True, True)

elif sAction == "remove" or sAction == 'delete':
    orderItem = OrderItem(iId, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    orderItem.delete()

    print "Content-Type: application/json\r\n\r\n"
    print '{ "data" : [ ]}'

elif sAction == "search":
    dStartDateTime = form.getvalue('startdatetime')
    dEndDateTime = form.getvalue('enddatetime')
    sStatus = form.getvalue('status')
    colorTimeSearch = ColorTimeSearch(dStartDateTime, dEndDateTime, sStatus)
    colorTimeSearch.search()
    custJson = colorTimeSearch.toJson()

    # insert options clause and closing brace
    returnJson = custJson

    print "Content-Type: application/json\r\n\r\n"
    print returnJson

elif sAction == "searchbyorderid":
    iOrderId = int(form.getvalue('orderid'))
    orderItemSearchByOrderId = OrderItemSearchByOrderId(iOrderId)
    orderItemSearchByOrderId.search()
    custJson = orderItemSearchByOrderId.toJson()

    # insert options clause and closing brace
    returnJson = custJson

    print "Content-Type: application/json\r\n\r\n"
    print returnJson

elif sAction == 'test':
    returnJson = '[  {    "title": "Ceramics",    "id": "821",    "start": "2017-07-24 09:00:00",    "end": "2017-07-24 10:30:00" , "color": "#000000" },   \
        { \
        "title": "Zippy", \
        "id": "822", \
        "start": "2017-07-24 10:00:00", \
        "end": "2017-07-24 11:30:00", \
        "color": "#FF0000" \
        } \
        ]'

    print "Content-Type: application/json\r\n\r\n"
    print returnJson

elif sAction == 'test2':
    returnJson = '{ "ColorTimes" : [ { "status":"Active","colorid":"1","start":"2017-07-26 11:00:00","end":"2017-07-26 09:30:00","id":"16","color":"#FF0000" }]}'

    print "Content-Type: application/json\r\n\r\n"
    print returnJson

else:
    print "Content-Type: text/plain\r\n\r\n"
    print "Invalid action: " + sAction
