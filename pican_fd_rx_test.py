#!/usr/bin/python3
#
# pican_fd_tx_test.py
#
# For use with PiCAN FD board
# http://skpang.co.uk/catalog/canbus-fd-board-with-real-time-clock-for-raspberry-pi-3-p-1545.html
#

import RPi.GPIO as GPIO
import os
import can
import time
led = 22
count = 0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,True)

print('\n\rCAN Tx test')
print('Bring up CAN0....')

# Bring up can0 interface at 500kbps / 2000kbps FD frame
os.system("sudo /sbin/ip link set can0 up type can bitrate 500000 dbitrate 2000000 fd on sample-point .8 dsample-point .8")
time.sleep(0.1)	

try:
	bus = can.interface.Bus(channel='can0', bustype='socketcan_native',fd = True)
except OSError:
	print('Cannot find PiCAN FD board.')
	GPIO.output(led,False)
	exit()
print('Ready')	

# Main loop
try:
	while True:
		message = bus.recv()	# Wait until a message is received.
		
		c = '{0:f} {1:x} {2:x} {3:x} {4:x} '.format(message.timestamp, message.is_fd,message.bitrate_switch,message.arbitration_id, message.dlc)
		s=''
		for i in range(message.dlc ):
			s +=  '{0:x} '.format(message.data[i])
			
		print(' {}'.format(c+s))
	
	
except KeyboardInterrupt:
	#Catch keyboard interrupt
	os.system("sudo /sbin/ip link set can0 down")
	print('\n\rKeyboard interrtupt')