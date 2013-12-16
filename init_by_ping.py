# -*- coding: cp936 -*- 
'''
Created on December 13th, 2013

For Windows only.
Using multi-thread(saving time) to check if a device is online by checking the return value of ping test.
If a device is online, the stdout may like this:
---
Pinging 192.168.1.1 with 32 bytes of data:

Reply from 192.168.1.1: bytes=32 time=1ms TTL=255

Ping statistics for 192.168.1.1:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 1ms, Average = 1ms
---
and if it's offline, stdout may like this:
---
Pinging 192.168.1.3 with 32 bytes of data:

Request timed out.

Ping statistics for 192.168.1.3:
    Packets: Sent = 1, Received = 0, Lost = 1 (100% loss),
---
So I get its status by searching 'success flag', both on Chinese & English Windows OS.

@author: Damon
'''


import subprocess
import threading
import GLOBAL

def ping_ip(index):
    ret = subprocess.Popen('ping -n 1 %s%d' %(GLOBAL.ipaddr, index), stdin = subprocess.PIPE, \
                           stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)

    output = ret.stdout.read()

    online_str1 = '往返行程的估计时间'
    online_str2 = 'Approximate round trip times in milli-seconds'

    #print output.find(err)

    ret = output.find(online_str1)
    if -1 == ret:
        ret = output.find(online_str2)

    if -1 == ret:
        return False
    else:
        return True

class check_if_online(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
    def run(self):
        ret = ping_ip(self.index)
        if True == ret:
            GLOBAL.enc_status[self.index] = 1
        else:
            GLOBAL.enc_status[self.index] = 0

def run():
    for name,address in GLOBAL.enc_status.items():
        t = check_if_online(name)
        t.start()
        t.join()

if __name__ == '__main__':
    print GLOBAL.enc_status
    run()
    print GLOBAL.enc_status

