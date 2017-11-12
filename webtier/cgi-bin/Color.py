#!/usr/bin/env python

# enable debugging
import cgitb
cgitb.enable()
import cgi

from Db.Color import Color
from Db.ColorSearch import ColorSearch

#print "Content-Type: text/plain\r\n\r\n"

# Gather url paramters
form = cgi.FieldStorage()
sAction = form.getvalue('action')

if sAction == 'create' or sAction == 'edit' or sAction == 'remove':
    sId = form.keys()[1][5:form.keys()[1].find('][')]
    iId = int(sId)
    sCode = str(form.getvalue('data[' + sId + '][code]'))
    sDescription = str(form.getvalue('data['+sId+'][description]'))
    sHexcode = str(form.getvalue('data[' + sId + '][hexcode]'))
    sStatus = str(form.getvalue('data['+sId+'][status]'))

if sAction == 'get':
    iId = str(form.getvalue("id"))

if sAction == None:
    print "Content-Type: text/plain\r\n\r\n"
    print "Missing action parameter.  Valid values are get, create, edit, and remove"

elif sAction == "get":

    color = Color(iId, '', '', '', '')
    color.load()

    print "Content-Type: application/json\r\n\r\n"
    print color.toJson('data', False, True)

elif sAction == "create" or sAction == "edit":
    color = Color(iId, sCode, sDescription, sHexcode, sStatus)
    color.save()

    print "Content-Type: application/json\r\n\r\n"
    print color.toJson('data', True, True)

elif sAction == "remove":
    color = Color(iId, '', '', '', '')
    color.delete()

    print "Content-Type: application/json\r\n\r\n"
    print '{ "data" : [ ]}'

elif sAction == "search":
    sStatus = form.getvalue('status')
    colorSearch = ColorSearch(sStatus)
    colorSearch.search()

    print "Content-Type: application/json\r\n\r\n"
    print colorSearch.toJson()

else:
    print "Content-Type: text/plain\r\n\r\n"
    print "Invalid action: " + sAction





