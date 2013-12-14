# -*- coding: cp936 -*- 
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
    if ret == -1:
        ret = output.find(online_str2)

    if ret == -1:
        return False
    else:
        return True

class check_if_online(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
    def run(self):
        ret = ping_ip(self.index)
        if ret == True:
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

