import os
import GLOBAL

keyword_arr = ['Called Memory smash',
'A packet data pointer has size',
'Call Trace',
'NMI Watchdog interrupt',
'Unable to handle kernel',
'Segmentation fault',
'bus error',
'Failed WQE allocate',
'UBIFS error',
'ECC'
]

filelist = ['disk',
'led',
'nic'
]

# return  inexiste:-1 error/null:0 right:1
def filecheck(int_val):
    #filename = str(int_val)
    for file in filelist:
        filename = ''
        filename = './log/round' + str(GLOBAL.round) + '/' + str(int_val) + '_' + file
        #print filename
        if os.path.exists(filename) == False:
            return -1
        if os.path.getsize(filename) == 0:
            return 0
        f = open(filename, 'r')
        while True:
            line = f.readline()
            if len(line) == 0:
                f.close()
                break
            for keyword in keyword_arr:
                if line.find(keyword) != -1:
                    f.close()
                    return 0
    return 1

if __name__ == '__main__':
    ret = filecheck(19)
    print ret
    #ret = filecheck(2)
    #print ret
    #ret = filecheck(3)
    #print ret
    #ret = filecheck(4)
    #print ret

