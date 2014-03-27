# -*- coding: cp936 -*- 
'''
Created on December 13th, 2013

log analysis module
Analysising log with error keywords, currently only return 3 status

@author: XieDongsheng, Damon
'''


import os
import GLOBAL
import re

temp_re = re.compile(r'(\d+?) C')
power_re = re.compile(r'(?: left|right)\s+?(\S+?)\s+?(\S+?)\s+?(\S+?)\s+?(\S+?)\s+?')
packet_loss_re = re.compile(r'transmitted, \d received, (\d+?)\% packet loss')
rate_re = re.compile(r'(\d+?)KB\/s')

keyword_arr = ['Called Memory smash',
               '404 - Not Found',
               'A packet data pointer has size',
               'Call Trace',
               'NMI Watchdog interrupt',
               'Unable to handle kernel',
               'Segmentation fault',
               'bus error',
               'Failed WQE allocate',
               'UBIFS error',
               'ECC',
               'Unhandled error code',
               'Sense Key',
               'Connection timed out',
               'AC is failed',
               'Link up with 100 Mbps',
               'Link up with 10 Mbps',
               'Half duplex',
               'eeprom is error',
               'power supply: unpresent',
               'unpresent',
               'No route to host',
               'get object_id',
               'rate changed  to'
               ]


# return  inexiste:-1 error/null:0 right:1
def filecheck(filename):
	#print filename
	if os.path.exists(filename) == False:
		return -1
	if os.path.getsize(filename) == 0:
		return 0
	f = open(filename, 'r')
	i = 1
	while True:
		line = f.readline()
		if len(line) == 0:
			f.close()
			break
		for keyword in keyword_arr:
			if line.find(keyword) != -1:
				print i, keyword
				GLOBAL.err_row = i
				GLOBAL.err_msg = keyword
				f.close()
				return 0
		for x in temp_re.findall(line):
			if int(x) <= 0 or int(x) >=60:
				GLOBAL.err_row = i
				GLOBAL.err_msg = 'temperatue error'
				f.close()
				return 0
		for y in power_re.findall(line):
			if y[0] != 'true' or y[1] != 'true' or y[2] != 'false' or y[3] != 'false':
				GLOBAL.err_row = i
				GLOBAL.err_msg = 'power error'
				f.close()
				return 0
		for z in packet_loss_re.findall(line):
			if int(z) > 0:
				GLOBAL.err_row = i
				GLOBAL.err_msg = 'ping package loss'
				f.close()
				return 0
		for m in rate_re.findall(line):
			if int(m) == 0:
				GLOBAL.err_row = i
				GLOBAL.err_msg = 'net rate is 0KB/s'
				f.close()
				return 0
		i += 1
	return 1

if __name__ == '__main__':
    GLOBAL.test_round = 1
    ret = filecheck('./log/round1/158_heat')
    print ret

