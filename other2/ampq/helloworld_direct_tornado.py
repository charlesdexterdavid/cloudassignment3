from __future__ import print_function
# from proton import Message
from proton.handlers import MessagingHandler
from proton_tornado import Container

class HelloWorld(MessagingHandler):
    def __init__(self, url):
        super(HelloWorld, self).__init__()
        self.url = url

    def on_start(self, event):
        self.acceptor = event.container.listen(self.url)
        event.container.create_sender(self.url)

    def on_sendable(self, event):
        event.sender.send(Message(body="Hello World!"))
        event.sender.close()

    def on_message(self, event):
        print(event.message.body)

    def on_accepted(self, event):
        event.connection.close()

    def on_connection_closed(self, event):
        self.acceptor.close()

Container(HelloWorld("localhost:8888/examples")).run()

# https://qpid.apache.org/releases/qpid-proton-0.10/proton/python/tutorial/tutorial.html