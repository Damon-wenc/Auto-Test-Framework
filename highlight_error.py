# -*- coding: cp936 -*- 
'''
Created on March 27th, 2014

Automatically show error info among a various of log files

@author: Damon
'''

import os
import time

def run():
    checked_round = 0
    interval = 60# * 3

    while True:
        checking_round = 0
        log_path = os.path.join(os.getcwd(), 'log')
        for i in os.listdir(log_path):
            if i.find('round') == 0:
                #print checking_round, checked_round
                checking_round += 1
                if checking_round <= checked_round: #log folders have already been checked
                    continue
                #print checking_round, checked_round
                for j in os.listdir(os.path.join(log_path, i)):
                    print j
                checked_round += 1
        time.sleep(10)

        #break
        


if __name__ == '__main__':
    run()
