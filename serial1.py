import serial
import time

arduino = serial.Serial("/dev/ttyUSB0", 9600, timeout = 0.00001, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, xonxoff = 0, rtscts = 0);


time.sleep(1)

print ("Iniciando")
con = 1





while (1):
	if(con == 1):
		data = arduino.read_until('1')
		time.sleep(1)

		print (data)

	time.sleep(1)




