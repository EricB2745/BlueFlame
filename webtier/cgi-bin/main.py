#!/usr/bin/env python

# enable debugging
import cgitb
cgitb.enable()

print "Content-Type: text/plain\r\n\r\n"

from Db.OrderStatus import OrderStatus

orderStatus = OrderStatus(4, '', '')
orderStatus.load()

print orderStatus.id
print orderStatus.description
print orderStatus.status

# insert new
orderStatus.id = 0
orderStatus.description = 'yet another status 4'
orderStatus.save()

print orderStatus.id
print orderStatus.description
print orderStatus.status

# update existing
#orderStatus.id = 11
#orderStatus.description = 'updated status'
#orderStatus.save()
