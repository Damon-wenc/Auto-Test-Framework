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


def run(enc_index, cmd):
    connect = subp.Popen(["plink.exe", '-ssh', 'root@%s%s' %(GLOBAL.ipaddr, enc_index), '-pw', 'root'],\
                         stdout=subp.PIPE, stderr=subp.PIPE, stdin=subp.PIPE)
    connect.stdin.write("login -n admin -p admin\n")
    connect.stdin.write("hwtest -t %s\n" %cmd)
    connect.stdin.write("quit\n")
    connect.wait()


if __name__ == '__main__':
    run(19, 'start')
