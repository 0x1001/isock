from isock import Server
from isock import Client
from isock import Handler

class Echo(Handler):
    def handle(self):
        data = self.receive()
        self.send(data)
        self.close()


Server("localhost",4440,Echo).start()

print Client("localhost",4440).send("aAaAaA")


################################################################################
from isock import Command

class Action1(Command):
    def action(self,data):
        return data

class Action2(Command):
    def __init__(self,server_var):
        self.server_var = server_var

    def action(self,data):
        pass

class Action3(Command):
    def action(self,data):
        pass

server = Server("localhost",4440)
server.registerCommand(Action1())
server.registerCommand(Action2(server_var))
server.registerCommand(Action3())
server.start()

client = Client("localhost",4440)
returned_data = client.executeCommand(Action1,data) #echo
returned_data = client.executeCommand(Action2,data)
returned_data = client.executeCommand(Action3,data)