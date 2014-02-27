from isock import Server
from isock import Client
from isock import Handler

class Echo(Handler):
    def handle(self):
        data = self.receive()
        self.send(data)
        self.close()