# -*- coding: cp936 -*- 
'''
Created on March 27th, 2014

Automatically show error info among a various of log files

@author: Damon
'''

import os
import GLOBAL
import time

def run():
    log_round = 0
    interval = 60# * 3

    while True:
        if log_round > GLOBAL.test_round: #it means a new test loop begin
            print "*" * 30
            log_round = 1

        if log_round == GLOBAL.test_round:
            time.sleep(interval)

        log_path = os.path.join(os.getcwd(), 'log')
        for i in os.listdir(log_path):
            if i.find('round') == 0:
                log_round += 1
                tmp_round = 0
                if tmp_round == log_round:
                    continue
                for j in os.listdir(os.path.join(log_path, i)):
                    print j
                tmp_round += 1

        break
        time.sleep(3)


if __name__ == '__main__':
    run()
