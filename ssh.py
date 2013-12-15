# -*- coding: cp936 -*- 

import subprocess as subp
import GLOBAL


def run(enc_index, cmd):
    connect = subp.Popen(["plink.exe", '-ssh', 'root@%s%s' %(GLOBAL.ipaddr, enc_index), '-pw', 'root'],\
                         stdout=subp.PIPE, stderr=subp.PIPE, stdin=subp.PIPE)
    connect.stdin.write("login -n admin -p admin\n")
    connect.stdin.write("hwtest -t %s\n" %cmd)
    connect.stdin.write("quit\n")


if __name__ == '__main__':
    run(19, 'start')
