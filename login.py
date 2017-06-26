#!/usr/bin/python2

import cgi
print "Content-type:text/html\r\n\r\n"
print "";
data=cgi.FieldStorage()
#print data
username=data.getvalue('usr')
password=data.getvalue('pass')
if username=='root' and password=='redhat':
	#print "<META HTTP-EQUIV='refresh' content='0 url=/services.html' />"
	print "<a href=/services.html>"
	print "click here"
	print "</a>"
 
else:
	print "plz enter valid details  </br></br>"
	#print "<META HTTP-EQUIV='refresh' content='0 url=/index.html' />"
	print "<a href=http://192.168.122.1/index.html>"
	print "click here to redirect"
	print "</a>"
