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
        
def get_log():
    thread_pool = []
    for name, address in GLOBAL.enc_status.items():
        if 1 == address:
            thread_pool.append(retrieve_log(name, 'heat'))
    for t in thread_pool:
        t.start()
        #time.sleep(5)
    for t in thread_pool:
        t.join()

class check_log_status(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
    def run(self):
        filename = ''
        filename = './log/round' + str(GLOBAL.test_round) + '/' + str(self.index) + '_heat'
        ret = analysis.filecheck(filename)
        if 1 == ret:
            GLOBAL.enc_status[self.index] = 1
        else:
            GLOBAL.enc_status[self.index] = -1

def check_log():
    thread_pool = []
    for name, address in GLOBAL.enc_status.items():
        if 1 == address:
            thread_pool.append(check_log_status(name))
    for t in thread_pool:
        t.start()
        time.sleep(1)
    for t in thread_pool:
        t.join()
                    
def send_cmd(cmd):
    thread_pool = []
    for name, address in GLOBAL.enc_status.items():
        if 'start' == cmd:
            if 1 == address:
                thd = threading.Thread(target = ssh.run, args = (name, cmd))
                thread_pool.append(thd)
        else:
            if 0 != address:
                thd = threading.Thread(target = ssh.run, args = (name, cmd))
                thread_pool.append(thd)
    
    for t in thread_pool:
        t.start()
        time.sleep(1)
    for t in thread_pool:
        t.join()

def set_log_dir():
    for name, address in GLOBAL.enc_status.items():
        if 1 == address:
            GLOBAL.log_dir[name] = GLOBAL.test_round

def start():
    if 1 == GLOBAL.test_round:
        send_cmd('start')
        time.sleep(90)
    set_log_dir()
    get_log()
    check_log()

    
def stop():
    send_cmd('stop')

if __name__ == '__main__':
    GLOBAL.enc_status = {19 : 1}
    stop()
