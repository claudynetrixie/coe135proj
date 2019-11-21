#!/usr/bin/env python
import subprocess
import os
import time


import pyudev
from subprocess import call

print("Code started. with pid " + str(os.getpid()) + "\n");
ctr = 0
context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

for device in iter(monitor.poll, None):
    if device.action == 'add':
        time.sleep(1)
        ctr = ctr + 1
        print("TRIGGERED " + str(ctr))
        #print('{} connected'.format(device))
	    #call(["usr/bin/sudo", "/usr/bin/python", "serial1.py"])
        if (ctr <= 1):
            cmd1 = subprocess.Popen(["python", "serial1.py", "-f"])
            print("spawned " + str(cmd1) + "\n");
            print('{0} ({1})'.format(device.device_node, device.device_type))
        else:
            ctr = 0
        # do something very interesting here.
	#print('{0} ({1})'.format(device['DEVNAME'], device['DEVTYPE']))
