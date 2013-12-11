import os
import GLOBAL

keyword_arr = ['error',
'shit',
'fuck'
]

# return   inexiste:-1   error/null:0    right:1
def filecheck(int_val):
    filename = str(int_val)
    filename = './log/round' + str(GLOBAL.round) + '/' + filename
    if os.path.exists(filename) == False:
        return -1
    if os.path.getsize(filename) == 0:
        return 0
    f = open(filename, 'r')
    while True:
        line = f.readline()
        if len(line) == 0:
            f.close()
            return 1
        for keyword in keyword_arr:
            if line.find(keyword) != -1:
                f.close()
                return 0


if __name__ == '__main__':
    ret = filecheck(1)
    print ret
    ret = filecheck(2)
    print ret
    ret = filecheck(3)
    print ret
    ret = filecheck(4)
    print ret
    ret = filecheck(5)
    print ret
    ret = filecheck(6)
    print ret
    ret = filecheck(7)
    print ret
    ret = filecheck(8)
    print ret
    ret = filecheck(9)
    print ret
    ret = filecheck(10)
    print ret

