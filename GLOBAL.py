# -*- coding: cp936 -*- 
'''
Created on December 13th, 2013

Global variables in multi files

@author: Damon
'''


#The number of devices you want to run test on
max_enc = 100

#this dict stores device status
#currently only three possible values, 0:offline, 1:good, -1:error  
enc_status = {}
for i in range (101, max_enc + 101):
    enc_status[i] = 0

#I use the prefix with index to compose a complete ip address, like '192.168.2.1', '192.168.2.2' 
ipaddr = '192.168.2.'

#
interval = 60 * 30 #30 minutes

#
test_round = 1
