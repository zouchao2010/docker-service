# -*- coding: utf-8 -*-
import datetime
import signal
import time
import sys
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.log import gen_log
from tornado.options import parse_command_line


def run_server():
    parse_command_line()

    @gen.coroutine
    def callback():
        try:
            while True:
                gen_log.info(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                time.sleep(1)
        except:
            pass

    def exit(*args):
        gen_log.info("Service Exit! signal:{}".format(args[0]))
        IOLoop.instance().stop()
        sys.exit(0)

    signal.signal(signal.SIGINT, exit)
    signal.signal(signal.SIGTERM, exit)

    IOLoop.instance().add_callback(callback)
    IOLoop.instance().start()

if __name__ == '__main__':
    try:
        print "Service Start!"
        run_server()
    except KeyboardInterrupt:
        print "Service Stop!"
