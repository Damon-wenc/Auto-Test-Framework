import subprocess as subp


def run(enc_index, cmd):
    connect = subp.Popen(["plink.exe", '-ssh', 'root@192.168.1.%s' %enc_index, '-pw', 'root'],\
                         stdout=subp.PIPE, stderr=subp.PIPE, stdin=subp.PIPE)
    connect.stdin.write("login -n admin -p admin\n")
    connect.stdin.write("hwtest -t %s\n" %cmd)
    #connect.stdin.write("nicipset -e eth3 -i 192.168.12.19\n")
    connect.stdin.write("quit\n")


if __name__ == '__main__':
    run(19, 'start')
