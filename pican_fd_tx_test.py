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
	

# Main loop
for m in range(0,16):
     msg = can.Message(arbitration_id=0x7de,is_fd = True,bitrate_switch = True,data=[0,0,0,0,0,0x1e,0x21,0xfe, 0x80, 0, 0,m, 0],extended_id=False)
     bus.send(msg)
     print(m)
     time.sleep(0.02)
time.sleep(0.05)
os.system("sudo /sbin/ip link set can0 down")
GPIO.output(led,False)
