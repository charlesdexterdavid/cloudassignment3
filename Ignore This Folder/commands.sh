notddc@notddc000000:~$ Top
notddc@notddc000000:~$ clear
notddc@notddc000000:~$ sudo systemctl stop workserver
notddc@notddc000000:~$ ls
notddc@notddc000000:~$ ls /srv
workserver
notddc@notddc000000:~$ more workserver
more: stat of workserver failed: No such file or directory
notddc@notddc000000:~$ cd workserver
-bash: cd: workserver: No such file or directory
notddc@notddc000000:~$ ls
notddc@notddc000000:~$ cd /srv/workserver
notddc@notddc000000:/srv/workserver$ ls
workserver.py
notddc@notddc000000:/srv/workserver$ nano workserver.py
notddc@notddc000000:/srv/workserver$ more workserver.py
more: cannot open workserver.py: Permission denied
notddc@notddc000000:/srv/workserver$ sudo more workserver.py
import math
import socket
import threading
import time
import requests
from bottle import route, run
from azure.servicebus import ServiceBusService, Message, Queue
hostname = socket.gethostname()
hostport = 9000
keepworking = False



def workerthread():

    bus_service = ServiceBusService(
    service_namespace='cloudassignment34ed0',
    shared_access_key_name='RootManageSharedAccessKey',
    shared_access_key_value='P6TUMCQVFg8ZIG8Z5KiPAIFaAHzvTcX9g7n8fNYAbZ0=')

    while (True):
        while (keepworking == True):
            # msg = bus_service.receive_queue_message('taskqueue', peek_lock=True)
            # print msg
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
notddc@notddc000000:/srv/workserver$
