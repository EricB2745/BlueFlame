#!/usr/bin/env python

# enable debugging
import cgitb
cgitb.enable()
import cgi

from Db.ColorTime import ColorTime
from Db.ColorTimeSearch import ColorTimeSearch

#print "Content-Type: text/plain\r\n\r\n"

# Gather url paramters
form = cgi.FieldStorage()
sAction = form.getvalue('action')

if sAction == 'add' or sAction == 'modify' or sAction == 'delete':  #simple add from get

    iId = int(form.getvalue('id'))
    iColorId = form.getvalue('colorid')
    dStartDateTime = form.getvalue('startdatetime')
    dEndDateTime = form.getvalue('enddatetime')
    sStatus = form.getvalue('status')

if sAction == 'create' or sAction == 'edit' or sAction == 'remove':
    sId = form.keys()[1][5:form.keys()[1].find('][')]
    iId = int(sId)
    iColorId = str(form.getvalue('data['+sId+'][colorid]'))
    dStartDateTime = form.getvalue('data['+sId+'][startdatetime]')
    dEndDateTime = str(form.getvalue('data[' + sId + '][enddatetime]'))
    sStatus = str(form.getvalue('data[' + sId + '][status]'))

if sAction == 'get':
    iId = str(form.getvalue("id"))

if sAction == None:
    print "Content-Type: text/plain\r\n\r\n"
    print "Missing action parameter.  Valid values are get, create, edit, and remove"

elif sAction == "get":

    colorTime = ColorTime(iId, '', '', '', '')
    colorTime.load()

    print "Content-Type: application/json\r\n\r\n"
    print colorTime.toJson('data', False, True)

elif sAction == "create" or sAction == "edit" or sAction=="add" or sAction == "modify":
    colorTime = ColorTime(iId, iColorId, dStartDateTime, dEndDateTime, sStatus)
    colorTime.save()

    print "Content-Type: application/json\r\n\r\n"
    print colorTime.toJson('data', True, True)

elif sAction == "remove" or sAction == 'delete':
    colorTime = ColorTime(iId, '', '', '', '')
    colorTime.delete()

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

elif sAction == "searchforcalendar":
    dStartDateTime = form.getvalue('start')
    dEndDateTime = form.getvalue('end')
    sStatus = 'Active'
    colorTimeSearch = ColorTimeSearch(dStartDateTime, dEndDateTime, sStatus)
    colorTimeSearch.search()
    custJson = colorTimeSearch.toJsonForCalendar()

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
