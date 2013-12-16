# -*- coding: cp936 -*-
'''
Created on December 13th, 2013

My main function, invoking other modules.
I need a control centor to handle 100 devices at the same time, but I don't want to develop a complex win32 client, 
so I seek help from tornado(web), a clear, light and easy-maintainable web frame. 
Showing device status & test result with Green(OK), Red(error occurs) and Grey(offline)
For more tornado info, visit here: http://www.tornadoweb.org/en/stable/
I only build a simple version web with 4 buttons: init, start, stop, open_log.
    init:     run ping test to get the status of all the devices, record online ones for further test;
    start:    send start test cmd to device, and retrieve & analysis log every 30 minutes(invoked by web auto refresh), give warning if any error occurs;
    stop:     send stop test cmd to device, stop the test loop;
    open_log: open log dir for manual analysis.
Maybe some scripts works only on Windows, I haven't tested them on some other OS yet. 

@author: Damon
''' 


import os
import shutil
import time
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import GLOBAL
import init_by_ping
import webbrowser
import run_test


from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

value = {}
flag_run_test = False

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index_show.html")

class InitHandler(tornado.web.RequestHandler):
    def get(self):
        global value, flag_run_test
        value = {}
        flag_run_test = False
        test_prepare()
        init_by_ping.run()
        get_tag_value()
        self.render("test_result.html", flag = '<br/>', 
                    ctime=time.strftime('%H:%M %m-%d-%Y', time.localtime(time.time())), tround = 'initialization', 
                    tags = value
                    )

def get_tag_value():
    global value
    for name,address in GLOBAL.enc_status.items():
        if address == -1:
            value[name] = 'align=middle bgcolor="red"'
        elif address == 0:
            value[name] = 'align=middle bgcolor="grey"'
        else:
            value[name] = 'align=middle bgcolor="limegreen"'

def test_prepare():
    os.chdir('./log')
    dirs = os.listdir('.')
    pack_dir = 'timebefore%s' %time.strftime('%H_%M_%m_%d_%Y', time.localtime(time.time()))
    
    for folder in dirs:
        if 0 != folder.find('timebefore'):
            if False == os.path.exists(pack_dir):
                os.mkdir(pack_dir)
            shutil.move(folder, pack_dir)
    
    os.chdir('..')

class OpenlogHandler(tornado.web.RequestHandler):
    def get(self):
        log_path = os.getcwd()
        os.system("explorer.exe %s\log" %log_path)
    
class StopHandler(tornado.web.RequestHandler):
    def get(self):
        global flag_run_test
        flag_run_test = False
        run_test.stop()
        self.render("stop.html")
        
        
class StartHandler(tornado.web.RequestHandler):
    def get(self):
        global flag_run_test, value
        if 1 == GLOBAL.test_round:
            flag_run_test = True
        if flag_run_test:
            web_refresh = '<head><meta http-equiv="refresh" content="' + str(GLOBAL.interval) + '"></head>'
        else:
            web_refresh = '<br/>'
        print flag_run_test
        value = {}
        os.makedirs("log/round%d" %GLOBAL.test_round)
        run_test.start()
        get_tag_value()
        self.render("test_result.html", flag = web_refresh, 
                    ctime = time.strftime('%H:%M %m-%d-%Y', time.localtime(time.time())), tround = GLOBAL.test_round, 
                    tags = value
                    )  
        GLOBAL.test_round += 1


def main():
    tornado.options.parse_command_line()
    webbrowser.open_new_tab('http://localhost:8888')
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/init", InitHandler),
        (r"/run", StartHandler),
        (r"/stop", StopHandler),
        (r"/open_log", OpenlogHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
    )
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
