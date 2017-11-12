#!/usr/bin/env python

# enable debugging
import cgitb
cgitb.enable()
import cgi

from Db.Activity import Activity
from Db.ActivitySearch import ActivitySearch

#print "Content-Type: text/plain\r\n\r\n"

# Gather url paramters
form = cgi.FieldStorage()
sAction = form.getvalue('action')

if sAction == 'create' or sAction == 'edit' or sAction == 'remove':
    sId = form.keys()[1][5:form.keys()[1].find('][')]
    iId = int(sId)
    sName = str(form.getvalue('data[' + sId + '][name]'))
    sDescription = str(form.getvalue('data['+sId+'][description]'))
    sStatus = str(form.getvalue('data['+sId+'][status]'))

if sAction == 'get':
    iId = str(form.getvalue("id"))

if sAction == None:
    print "Content-Type: text/plain\r\n\r\n"
    print "Missing action parameter.  Valid values are get, create, edit, and remove"

elif sAction == "get":

    activity = Activity(iId, '', '', '')
    activity.load()

    print "Content-Type: application/json\r\n\r\n"
    print activity.toJson('data', False, True)

elif sAction == "create" or sAction == "edit":
    activity = Activity(iId, sName, sDescription, sStatus)
    activity.save()

    print "Content-Type: application/json\r\n\r\n"
    print activity.toJson('data', True, True)

elif sAction == "remove":
    activity = Activity(iId, '', '', '')
    activity.delete()

    print "Content-Type: application/json\r\n\r\n"
    print '{ "data" : [ ]}'

elif sAction == "search":
    sStatus = form.getvalue('status')
    activitySearch = ActivitySearch(sStatus)
    activitySearch.search()

    print "Content-Type: application/json\r\n\r\n"
    print activitySearch.toJson()

else:
    print "Content-Type: text/plain\r\n\r\n"
    print "Invalid action: " + sAction





