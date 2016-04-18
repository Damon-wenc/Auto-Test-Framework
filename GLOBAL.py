# -*- coding: cp936 -*- 
'''
Created on December 13th, 2013

Global variables sharing in multi files

@author: Damon
'''
from collections import OrderedDict

#The number of devices you want to run test on
max_enc = 100

#ip range
start_ip = 101
end_ip   = 101 + max_enc

#this dict stores device status
#currently only three possible values, 0:offline, 1:good, -1:error  
enc_status = OrderedDict()
for i in range (start_ip, end_ip):
    enc_status[i] = 0

#this dict stores the latest log round for each device. I'm trying to create a 'open log dir' link with this dict.
#i.e. ,when test starts, the address of all online devices are set to 1, and if any devices fails, the address value stops increasing.
#So its value is equal with the latest round, or the round error occured.
log_dir = OrderedDict()
for i in range (start_ip, end_ip):
    log_dir[i] = 0

#I use a prefix + index to compose a complete ip address, like '192.168.2.101', '192.168.2.202' 
ipaddr = '192.168.2.'

#
interval = 60 * 3 #3 minutes, the interval SHOULD NOT BE LESS THAN 3 MINITES!!! (that's the time of one-round costs)

#
test_round = 1

#for auto show error info function
err_row = 0
err_msg = ""
