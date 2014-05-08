# -*- coding: cp936 -*- 
'''
Created on December 13th, 2013

This file defines my method to connect to device.
Usually, using 'paramiko' or 'Pexpect' module is better at most cases, but my device got a weird ssh server, 
it can't response to the two above modules, so I've got to try using a third party software.
Of course on Windows only.

@author: Damon
'''

import subprocess as subp
import GLOBAL
import time


def run(enc_index, cmd):
    if 'start' == cmd:
        retry_times = 1
    else:
        retry_times = 20
    count = 0
    
    connect = subp.Popen(["plink.exe", '-ssh', 'root@%s%s' %(GLOBAL.ipaddr, enc_index), '-pw', 'root'],\
                         stdin=subp.PIPE)
    if 'start' == cmd:
        time.sleep(10)
        connect.stdin.write("y\n")
    time.sleep(3)
    connect.stdin.write("login -n admin -p admin\n")
    time.sleep(3)
    connect.stdin.write("hwtest -t %s\n" %cmd)
    time.sleep(3)
    connect.stdin.write("quit\n")
    time.sleep(30)
    #connect.wait()
    while True:
        if 0 == connect.poll():
            break
        elif retry_times == count:
            break
        else:
            connect.kill()
            connect = subp.Popen(["plink.exe", '-ssh', 'root@%s%s' %(GLOBAL.ipaddr, enc_index), '-pw', 'root'],\
                         stdout=subp.PIPE, stderr=subp.PIPE, stdin=subp.PIPE)
            connect.stdin.write("y\n")
            connect.stdin.write("login -n admin -p admin\n")
            connect.stdin.write("hwtest -t %s\n" %cmd)
            connect.stdin.write("quit\n")
            count += 1
            time.sleep(60)
            #connect.wait()
            


if __name__ == '__main__':
    run(19, 'start')
