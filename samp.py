#!/usr/bin/env python
import subprocess

sudo_password = 'mysecretpass'


import pyudev
from subprocess import call


context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

for device in iter(monitor.poll, None):
    if device.action == 'add':
        #print('{} connected'.format(device))
	#call(["usr/bin/sudo", "/usr/bin/python", "serial1.py"])
	cmd1 = subprocess.Popen(["sudo", "python", "serial1.py", "-f"])
	print('{0} ({1})'.format(device.device_node, device.device_type))
        # do something very interesting here.
	#print('{0} ({1})'.format(device['DEVNAME'], device['DEVTYPE']))
