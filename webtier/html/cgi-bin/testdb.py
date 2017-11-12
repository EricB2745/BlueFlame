#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","local","loc@l!","BlueFlame" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "CALL Customer_Type_Get(1);"

try:
  	# Execute the SQL command
  	cursor.execute(sql)
  	# Fetch all the rows in a list of lists.
  	row = cursor.fetchone()
  	print row[0]
	print row[1]
	print row[2]

except:
   print "Error: unable to fecth data"

# close cursor
cursor.close() 
# disconnect from server
db.close()
