#!/usr/bin/python2

import cgi
print "Content-type:text/html"
print ""
x=cgi.FieldStorage()

data=x.getvalue('ch')


if data=="firefox":
	print "<a href=http://192.168.122.1/firefox.sh>"
	print "click here"
	print "</a>"
elif data=="gedit":
	print "<a href=http://192.168.122.1/gedit.sh>"
	print "click here"
	print "</a>"
elif data=="vlc":
	print "<a href=http://192.168.122.1/vlc.sh>"
	print "click here"
	print "</a>"
elif data=="calc":
	print "<a href=http://192.168.122.1/calc.sh>"
	print "click here"
	print "</a>"
elif data=="webcam":
	print "<a href=http://192.168.122.1/webcam.sh>"
	print "click here"
	print "</a>"
elif data=="screenshot":
	print "<a href=http://192.168.122.1/screenshot.sh>"
	print "click here"
	print "</a>"
elif data=="office":
	print "<a href=http://192.168.122.1/office.sh>"
	print "click here"
	print "</a>"


else:
	print "not found"
