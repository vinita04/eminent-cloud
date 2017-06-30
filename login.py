#!/usr/bin/python2

import cgi,cgitb,time
import mysql.connector as mariadb 
print "Content-type:text/html\r\n\r\n"
print "";
cgitb.enable()
#recv data from html page
data=cgi.FieldStorage()
mariadb_connection = mariadb.connect(user='root', password='redhat', database='cloud')
cursor = mariadb_connection.cursor()

#store recvd data
username=data.getvalue('usr')
password=data.getvalue('pass')


cursor.execute("SELECT name,password from user WHERE name = %s && password = %s", (username,password))
data = cursor.fetchone()

if data==None:
	print "plz enter correct details"
	time.sleep(3)
	print "<META HTTP-EQUIV='refresh' content='0; url=/index.html' />"
elif username==data[0] and password==data[1] :
	print "<META HTTP-EQUIV='refresh' content='0; url=/services.html' />"


mariadb_connection.close() 
'''except: 
	print "error"
	mariadb_connection.rollback()'''

	#
  #if username=='root' and password=='redhat':
	
	#print "<a href=/services.html>"
	#print "click here"
	#print "</a>"
 
'''else:
	print "plz enter valid details  </br></br>"
	'''
	#print "<a href=http://192.168.122.1/index.html>"
	#print "click here to redirect"
	#print "</a>"'''
