#!/usr/bin/env python
import subprocess
import os
import time
import pwd


import pyudev
from subprocess import call

user = str(pwd.getpwuid(os.getuid())[0])

print("Code started. with pid " + str(os.getpid()) + "\n");
ctr = 0
context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

for device in iter(monitor.poll, None):
    if device.action == 'add':
        time.sleep(1)
        ctr = ctr + 1
        if (ctr <= 1):
            cmd1 = subprocess.Popen(["python", "/home/" + user + "/Authduino/serial_read.py", "-f"])
            print('{0} ({1})'.format(device.device_node, device.device_type))
        else:
            ctr = 0
    if device.action == 'remove':
        ctr = ctr + 1
        if (ctr <= 1):
            print("USB Device Removed.\n")
            cmd2 = subprocess.Popen(["python", "/home/" + user + "/Authduino/key_detached.py", "-f"])
        else:
            ctr = 0
