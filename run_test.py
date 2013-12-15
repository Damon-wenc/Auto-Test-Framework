import GLOBAL
import analysis
import threading
import urllib
import ssh

class retrieve_log(threading.Thread):
    def __init__(self, index, name):
        threading.Thread.__init__(self)
        self.index = index
        self.url = 'http://192.168.1.' + str(index) + ':8081/upload/log_' + name
        self.name = str(index) + '_' + name
    def run(self):
        urllib.urlretrieve(self.url, "./log/round%d/%s" %(GLOBAL.round, self.name))
        
def get_log():
    for name,address in GLOBAL.enc_status.items():
        if address == 1:
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
        if ret == 1:
            GLOBAL.enc_status[self.index] = 1
        else:
            GLOBAL.enc_status[self.index] = -1

def check_log():
    for name,address in GLOBAL.enc_status.items():
        if address == 1:
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
        if address == 1:       
            t = enc_run_cmd(name, cmd)
            t.start()
            t.join()
        else:
            #print 'enc skipped'
            continue

def start():
    if 1 == GLOBAL.round:
        send_cmd('start')
    get_log()
    check_log()
    
def stop():
    send_cmd('stop')

if __name__ == '__main__':
    #print GLOBAL.enc_status
    #run()
    #print GLOBAL.enc_status
    GLOBAL.enc_status = {19 : 1}
    stop()
    #print GLOBAL.enc_status
