#!/usr/bin/env python

# enable debugging
import cgitb
cgitb.enable()

from Db.OrderStatus import OrderStatus

print "Content-Type: text/plain\r\n\r\n"

orderStatus = OrderStatus(4, '', '')
orderStatus.load()

print orderStatus.id
print orderStatus.description
print orderStatus.status

