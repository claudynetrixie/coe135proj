# Arduino USB Device Authentication in Linux

Our CoE 135 Final Project is to use an arduino device as a physical key to gain access to encrypted files in the Linux Operating System. The main goal of this project is to add a physical layer of security to important files. To accomplish this, a listener script written in python is created which interfaces with connected arduino(s) through PySerial and Pyudev.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What things you need to install the software and how to install them

```
Python 
Python PIP
PySerial python library
PyUdev python library 
Bcrypt python library
Arduino IDE
```

### Installing

A step by step series of examples that tell you how to get a development env running

Download python prerequisites using the following commands:
```
sudo apt install python
```
```
sudo apt install python-pip
```
```
sudo pip install pyudev
```
```
sudo pip install pyserial
```
```
sudo pip install bcrypt
```



Download Arduino IDE
```
$ tar –xf [Compressed-filename]
```
```
$ cd [Uncompressed-foldername]
```
```
$ sudo ./install.sh
```
```
$ sudo chown [username] [path/to/file]
```




Download Authduino.zip and authduino_installer.sh to obtain a copy of the pertinent files for the Arduino authentication. </br>
To install, run
```
sh authduino_installer.sh
```

Place files that you want to protect inside the directory
```
/home/$USER/AuthduinoDocs
```

## Running the tests

To test, plug in the Arduino device on a Linux computer. </br>
Observe that when the device is plugged in, the files inside the protected directory are decrypted. </br>

When the device is plugged out of the computer, the protected directory now has encrypted files.

### Further Tests

If the files are not being encrypted or decrypted, this can be debugged by checking the status of the authduino service. </br>
To do this, run
```
sudo systemctl status authduino.service
```


## Authors

Philippe Ivan S. Balucan 2016-01355
Claudyne Trixie G. Uy 2016-01189

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
