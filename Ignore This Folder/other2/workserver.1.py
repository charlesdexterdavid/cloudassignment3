import math
import socket
import threading
import time

from bottle import route, run

hostname = socket.gethostname()
hostport = 9000
keepworking = False  



def workerthread():
    while (True):
        while (keepworking == True):
            for x in range(1, 69):
                y = math.factorial(x)
        time.sleep(3)


# start the worker thread
worker_thread = threading.Thread(target=workerthread, args=())
worker_thread.start()


def writebody():
    body = '<html><head><title>Work interface - build</title></head>'
    body += '<body><h2>David Charles Worker interface on ' + hostname + '</h2><ul><h3>'

    if keepworking == False:
        body += '<br/>Worker thread is not running. <a href="./do_work">Start work</a><br/>'
    else:
        body += '<br/>Worker thread is running. <a href="./stop_work">Stop work</a><br/>'

    body += '<br/>Usage:<br/><br/>/do_work = start worker thread<br/>/stop_work = stop worker thread<br/>'
    body += '</h3></ul></body></html>'
    return body


@route('/')
def root():
    return writebody()


@route('/do_work')
def do_work():
    global keepworking
    # start worker thread
    keepworking = True
    return writebody()


@route('/stop_work')
def stop_work():
    global keepworking
    # stop worker thread
    keepworking = False
    return writebody()


run(host=hostname, port=hostport)
