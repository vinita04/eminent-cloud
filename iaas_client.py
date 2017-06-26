#!/usr/bin/python

import cgi,os
print "Content-type:text/html"
print ""
x=cgi.FieldStorage()


os_name=x.getvalue("osname")
os_ram=x.getvalue("osram")
os_cpu=x.getvalue("oscpu")
os_hdd=x.getvalue("oshdd")

if os_name=="kali":

	install_os='sudo virt-install --graphics vnc, listen=192.168.5.61,port=7654 --cdrom /root/Desktop/isoimage/kali/kali.iso --ram '+os_ram+' --vcpu '+os_cpu+' --nodisk --name '+os_name

	x=os.system(install_os)

	if x!=0:
		print "error"
elif os_name=="redhat":
	
	install_os1='sudo virt-install --graphics vnc, listen=192.168.5.61,port=7654 --cdrom /software/rhel7.2.iso --ram '+os_ram+' --vcpu '+os_cpu+' --nodisk --name '+os_name
	y=os.system(install_os1)

	if y!=0:
		print "error"


elif os_name=="centos":
	
	install_os2='sudo virt-install --graphics vnc, listen=192.168.5.61,port=7654 --cdrom /root/Desktop/isoimage/CentOS-7.0.iso --ram '+os_ram+' --vcpu '+os_cpu+' --nodisk --name '+os_name
	z=os.system(install_os2)

	if z!=0:
		print "error"

elif os_name=="ubuntu":
	
	install_os3='sudo virt-install --graphics vnc, listen=192.168.5.61,port=7654 --cdrom /root/Desktop/isoimage/ubuntu-16.04.iso --ram '+os_ram+' --vcpu '+os_cpu+' --nodisk --name '+os_name

	a=os.system(install_os3)

	if a!=0:
		print "error"


	
