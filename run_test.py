# -*- coding: cp936 -*- 
'''
Created on December 13th, 2013

Defines send_cmd, get_log and check_log functions, all of them are with multi-thread method
start function invokes send_cmd, get_log & check_log,
and stop funcion invokes send_cmd only

@author: Damon
'''

import GLOBAL
import analysis
import threading
import urllib
import ssh

class retrieve_log(threading.Thread):
    def __init__(self, index, name):
        threading.Thread.__init__(self)
        self.index = index
        self.url = 'http://%s'%GLOBAL.ipaddr + str(index) + ':8081/upload/log_' + name
        self.name = str(index) + '_' + name
    def run(self):
        urllib.urlretrieve(self.url, "./log/round%d/%s" %(GLOBAL.test_round, self.name))
        
def get_log():
    for name,address in GLOBAL.enc_status.items():
        if 1 == address:
            t1 = retrieve_log(name, 'disk')
            t2 = retrieve_log(name, 'led')
            t3 = retrieve_log(name, 'nic')
            t1.start()
            t2.start()
            t3.start()
            t1.join()
            t2.join()
            t3.join()
        else:
            #print 'enc absent'
            continue

class check_log_status(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
    def run(self):
        ret = analysis.filecheck(self.index)
        if 1 == ret:
            GLOBAL.enc_status[self.index] = 1
        else:
            GLOBAL.enc_status[self.index] = -1

def check_log():
    for name,address in GLOBAL.enc_status.items():
        if 1 == address:
            t = check_log_status(name)
            t.start()
            t.join()
        else:
            continue

class enc_run_cmd(threading.Thread):
    def __init__(self, name, cmd):
        threading.Thread.__init__(self)
        self.name = name
        self.cmd = cmd
    def run(self):
        print self.name
        ssh.run(self.name, self.cmd)
                    
def send_cmd(cmd):
    print GLOBAL.enc_status
    for name,address in GLOBAL.enc_status.items():
        if 1 == address:       
            t = enc_run_cmd(name, cmd)
            t.start()
            t.join()
        else:
            #print 'enc skipped'
            continue

def start():
    if 1 == GLOBAL.test_round:
        send_cmd('start')
    get_log()
    check_log()
    
def stop():
    send_cmd('stop')

if __name__ == '__main__':
    GLOBAL.enc_status = {19 : 1}
    stop()
