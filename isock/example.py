from isock import Server
from isock import Client
from isock import Handler

class Echo(Handler):
    def handle(self):
        data = self.receive()
        self.send(data)
        self.close()


Server("localhost",4440,Echo).serve_forever()

print Client("localhost",4440).send("aAaAaA")


################################################################################
from isock import Action

class Action1(Action):
    def action(self,data):
        return data

class Action2(Action):
    def __init__(self,server_var):
        self.server_var = server_var

    def action(self,data):
        pass

class Action3(Action):
    def action(self,data):
        pass

server = Server("localhost",4440)
server.registerCommand(Action1())
server.registerCommand(Action2(server_var))
server.registerCommand(Action3())
server.serve_forever()

client = Client("localhost",4440)
returned_data = client.executeCommand(Action1,data) #echo
returned_data = client.executeCommand(Action2,data)
returned_data = client.executeCommand(Action3,data)