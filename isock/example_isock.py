import threading
from isock import Server
from isock import Client
from isock import Action

################################################################################
############################ Server actions ####################################
################################################################################
class Echo(Action):
    def action(self,data):
        return data

class Exec(Action):
    def __init__(self,exec_history):
        self.exec_history = exec_history

    def action(self,data):
        import subprocess
        self.exec_history.append(data)
        return subprocess.check_output(data,shell=True)

class ExecHistory(Action):
    def __init__(self,exec_history):
        self.exec_history = exec_history

    def action(self,data):
        return self.exec_history

class Time(Action):
    def action(self,data):
        import datetime
        return datetime.datetime.now()

################################################################################
############################ Server startup ####################################
################################################################################
history = []

server = Server("localhost",4440)
server.registerAction(Echo())
server.registerAction(Exec(history))
server.registerAction(ExecHistory(history))
server.registerAction(Time())
server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()

################################################################################
############################ Client session ####################################
################################################################################

client = Client("localhost",4440)

print "############################# Echo test ################################"
print client.executeAction(Echo,"Echo test!")

print "############################# Exec test ################################"
print client.executeAction(Exec,"dir")
print client.executeAction(Exec,["python","-V"])

print "############################# Exec history #############################"
print client.executeAction(ExecHistory)

print "############################# Server time ##############################"
print client.executeAction(Time)

################################################################################
############################ Server shutdown ###################################
################################################################################
server.shutdown()
server_thread.join()
