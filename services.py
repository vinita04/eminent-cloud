#!/usr/bin/python2

import cgi
print "Content-type:text/html"
print ""
data=cgi.FieldStorage()

y=data.getvalue('s')


if y=="saas":
	print "<META HTTP-EQUIV='refresh' content='0 url=/saas.html' />"
	#print "<a href=http://192.168.122.1/saas.html>"
	#print "click here"
	#print "</a>"
elif y=="stass":
	print "<META HTTP-EQUIV='refresh' content='0 url=/staas.html' />"
	#print "<a href=http://192.168.122.1/staas.html>"
	#print "click here"
	#print "</a>"

elif y=="iaas":
	print "<a href=/iaas.html>"
	print "click here"
	print "</a>"
	
