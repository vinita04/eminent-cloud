#!/usr/bin/python2

import cgi,cgitb
import mysql.connector as mariadb
print "Content-type:text/html\r\n\r\n"
print ""
cgitb.enable()
#recv data from cloud
data=cgi.FieldStorage()
mariadb_connection = mariadb.connect(user='root', password='redhat', database='cloud')
cursor = mariadb_connection.cursor()

# get values from cloud 
u_name=data.getvalue('usr')
u_pass=data.getvalue('pass')
u_cpass=data.getvalue('cpass')
u_email=data.getvalue('email')

try:
	cursor.execute("INSERT INTO user (name,password,email) VALUES (%s,%s,%s)", (u_name,u_pass,u_email))
	mariadb_connection.commit() 
	mariadb_connection.close()
except: 
	print "error"
	mariadb_connection.rollback()

print "user is sucessfully created"
print "<META HTTP-EQUIV='refresh' content='0; url=/index.html' />"
#print "<a href=http://192.168.122.1/index.html>"
#print "click here"
#print "</a>"

