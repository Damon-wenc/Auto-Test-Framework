# -*- coding: cp936 -*- 
'''
Created on March 27th, 2014

Automatically show error info among a various of log files

@author: Damon
'''

import os
import time
import analysis
import GLOBAL
import threading

class analysis_log(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        k = analysis.filecheck(self.name)
        if k == 0:
            print '\n\n**********error detected**********'
            print 'error log url: \t%s' %self.name#os.path.join(i, j)
            print 'error row NO.: \tline %d' %GLOBAL.err_row
            print 'error keyword: \t%s\n\n' %GLOBAL.err_msg

def print_start():
    print '''
/************************************************************************
 *****************HEAT error log auto-detect program*********************
 *****************Please watch out for the upcoming prints***************
 ************************************************************************/
 '''
    
def run():
    interval = 60   #60 seconds, SHOULD NOT BE LESS THAN 60 SECONDS!!!
    n_last_round_folder = 0
    n_current_round_folder = 0
    checked_folders = []

    print_start()

    while True:
        log_path = os.path.join(os.getcwd(), 'log')
        dir_list = os.listdir(log_path)
        n_current_round_folder = len(dir_list)
        
        # if the count of folders decreased, it should be lots of 'old rounds' has been packed
        # so empty the checked_folders list
        if n_current_round_folder < n_last_round_folder:
            print checked_folders
            checked_folders = []
            print_start()
            
        for i in dir_list:
            if i.find('round') == 0:
                checked = False

                for folder in checked_folders:
                    if i == folder:
                        checked = True
                        break
                if checked:
                    continue
                #print '---', i
                thread_pool = []
                for j in os.listdir(os.path.join(log_path, i)):
                    thread_pool.append(analysis_log(os.path.join(log_path, i, j)))
                for x in thread_pool:
                    x.start()
                    #print len(thread_pool)
                for t in thread_pool:
                    t.join()
                    #k = analysis.filecheck(os.path.join(log_path, i, j))
                    #if k == 0:
                        #print '\n\n**********error detected**********'
                        #print 'error log url: \t%s' %os.path.join(i, j)
                        #print 'error row NO.: \tline %d' %GLOBAL.err_row
                        #print 'error keyword: \t%s\n\n' %GLOBAL.err_msg
                print "folder %s checked" %i
                checked_folders.append(i)
        #print '.'
        n_last_round_folder = n_current_round_folder
        time.sleep(10)
        #time.sleep(interval)

        


if __name__ == '__main__':
    run()
