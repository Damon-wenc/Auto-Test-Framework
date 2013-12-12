# -*- coding: cp936 -*- 
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
import urllib

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
        self.render("test_result.html", ctime=time.strftime('%H:%M %m-%d-%Y', time.localtime(time.time())), tround='initialization', 
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
        self.render("stop.html")
        #stop loop
        
class StartHandler(tornado.web.RequestHandler):
    def get(self):
        global flag_run_test, value
        flag_run_test = True
        value = {}
        os.makedirs("log/round%d" %GLOBAL.round)
        run_test.run()
        get_tag_value()
        self.render("test_result.html", ctime=time.strftime('%H:%M %m-%d-%Y', time.localtime(time.time())), tround=GLOBAL.round, 
                    tags = value
                    )    
        urllib.urlretrieve('http://localhost:8888/run?', 'log/round%d/result.html' %GLOBAL.round)    
        GLOBAL.round += 1
        #time.sleep(GLOBAL.interval)
        #time.sleep(10)


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
