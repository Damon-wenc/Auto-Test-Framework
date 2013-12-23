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
import time

class retrieve_log(threading.Thread):
    def __init__(self, index, name):
        threading.Thread.__init__(self)
        self.index = index
        self.url = 'http://%s'%GLOBAL.ipaddr + str(index) + ':8081/upload/log_' + name
        self.name = str(index) + '_' + name
    def run(self):
        urllib.urlretrieve(self.url, "./log/round%d/%s" %(GLOBAL.test_round, self.name))
        
def get_log(name):
    t1 = retrieve_log(name, 'heat')
    t1.start()
    t1.join()

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

def check_log(name):
    t = check_log_status(name)
    t.start()
    t.join()

class enc_run_cmd(threading.Thread):
    def __init__(self, name, cmd):
        threading.Thread.__init__(self)
        self.name = name
        self.cmd = cmd
    def run(self):
        ssh.run(self.name, self.cmd)
                    
def send_cmd(name, cmd):
    t = enc_run_cmd(name, cmd)
    t.start()
    t.join()

def set_log_dir(name):
    GLOBAL.log_dir[name] = GLOBAL.test_round

def start():
    for name, address in GLOBAL.enc_status.items():
        if 1 == address:
            if 1 == GLOBAL.test_round:
                send_cmd(name, 'start')
                time.sleep(15)
            get_log(name)
            check_log(name)
            set_log_dir(name)
    
def stop():
    for name, address in GLOBAL.enc_status.items():
        if 0 != address:
            send_cmd(name, 'stop')

if __name__ == '__main__':
    GLOBAL.enc_status = {19 : 1}
    stop()
