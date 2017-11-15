import math
import socket
import threading
import time
import requests
from bottle import route, run, template

hostname = socket.gethostname()
hostport = 9000
keepworking = False  



def workerthread():
    from azure.servicebus import ServiceBusService, Message, Queue
    bus_service = ServiceBusService(
    service_namespace='cloudassignment34ed0', 
    shared_access_key_name='RootManageSharedAccessKey',
    shared_access_key_value='P6TUMCQVFg8ZIG8Z5KiPAIFaAHzvTcX9g7n8fNYAbZ0=')
    
    while (True):
        while (keepworking == True):
            msg = bus_service.receive_queue_message('taskqueue', peek_lock=True)
            print msg 
        time.sleep(3)


# start the worker thread
worker_thread = threading.Thread(target=workerthread, args=())
worker_thread.start()


index_html = '''My first web app! By <strong>{{ author }}</strong>.'''
testoutput_html = '''<h2>Val{{ trans }}</h2>.'''







def writebody():
    body = '<html><head><title>Work interface - build</title></head>'
    body += '<body><h2>David Dexter Charles Worker interface on ' + hostname + '</h2><ul><h3>'

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


@route('/test')
def testoutput():
    return template(testoutput_html, trans='we will see')



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
