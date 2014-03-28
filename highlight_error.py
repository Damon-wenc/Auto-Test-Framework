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

def run():
    interval = 60   #60 seconds

    checked_round = 0
    checked_folders = []

    print '''
/********************************************************************************
 *********************ATF error log auto-detect program**************************
 *********************Please watch out for the upcoming prints*******************
 ********************************************************************************/
 '''

    while True:
        checking_round = 0
        log_path = os.path.join(os.getcwd(), 'log')
        for i in os.listdir(log_path):
            if i.find('round') == 0:
                checking_round += 1
                checked = False

                for folder in checked_folders:
                    if i == folder:
                        checked = True
                        break
                if checked:
                    continue
                #print '---', i
                for j in os.listdir(os.path.join(log_path, i)):
                    k = analysis.filecheck(os.path.join(log_path, i, j))
                    if k == 0:
                        print '\n\n**********error detected**********'
                        print 'error log url: \t%s' %os.path.join(i, j)
                        print 'error row NO.: \tline %d' %GLOBAL.err_row
                        print 'error keyword: \t%s\n\n' %GLOBAL.err_msg
                checked_round += 1
                checked_folders.append(i)
        #print '.'
        time.sleep(interval)

        


if __name__ == '__main__':
    run()
