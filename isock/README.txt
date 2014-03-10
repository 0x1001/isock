=======
iSocket
=======

**Simple client - server library based on TCP SocketServer**

iSocket is a library that allows very rapid development of client - server applications in Python.

If you develop software that runs on several machines which communicate with each other this library might come in handy.

Main features:

- Very simple server configuration.
- Easy way to transfer back and forth complex data structures (everything that is pickable can be send and receive).
- iSocket structure allows clean design of your application.
- Client can easily access variables on server.

iSocket is writen in Python 2.7 and works on Windows and Linux. Source code can be found here: https://github.com/0x1001/isock

iSocket installation
--------------------
::
    python setup.py install

iSocket example
---------------
Example shows how to create actions that server should perform for clients. Then how to start server and finally how to run client.

Actions that are defined in example:

- Echo - Sends back client all data
- Exec - Executes system call on server and transfers console output to client
- ExecHistory - Sends system call history to client
- Time - Sends server time to client
::
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
    server.addAction(Echo())
    server.addAction(Exec(history))
    server.addAction(ExecHistory(history))
    server.addAction(Time())
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()

    ################################################################################
    ############################ Client session ####################################
    ################################################################################
    client = Client("localhost",4440)

    print "############################# Echo test ################################"
    print client.runAction(Echo,"Echo test!")

    print "############################# Exec test ################################"
    print client.runAction(Exec,"dir")
    print client.runAction(Exec,["python","-V"])

    print "############################# Exec history #############################"
    print client.runAction(ExecHistory)

    print "############################# Server time ##############################"
    print client.runAction(Time)

    ################################################################################
    ############################ Server shutdown ###################################
    ################################################################################
    server.shutdown()
    server_thread.join()

iSocket server guide
--------------------
Server can be imported from isock::
    from isock import Server

Server constructor accepts two required arguments: ip (string) and port (int)::
    server = Server("localhost",4440)

To add actions to server use addAction method. It accepts one required argument: action (Action)::
    server.addAction(Echo())

To start server use serve_forever() blocking method::
    server.serve_forever()

To stop server use shutdown() method::
    server.shutdown()

iSocket client guide
--------------------
Client can be imported from isock::
    from isock import Client

Client constructor accepts two required arguments and one optional: server_ip (string), server_port (int), retry (int).
Default retry arguments is 3. Which allows 3 retries before ClientException is raised::
    client = Client("localhost",4440)

To run action on server use runAction() method which accepts one required argument and one optional: action (Action class ref), data (any pickable data)::
    client.runAction(Echo,"Echo test!")

Client method runAction() returns data send by server.

iSocket action guide
--------------------
All actions that server can perform have to inharite from Action class.
Action class can be imported from isock:
    from isock import Action

Both client and server have to have access to user defined action classes. It is suggested to keep them in separated file that is imported in both server and client.
To define new action create new class that inhertis from Action class and override action() method. This method accepts one required parameter: data (any pickable data send by client).
If client does not send any data this argument is set to None.
::
    class Echo(Action):
        def action(self,data):
            return data

Method action() returns data that are send back to client.

To access server variable in your action class define constructor that stores reference to server variable as attribute, which you can then access in action method::
    class ExecHistory(Action):
        def __init__(self,exec_history):
            self.exec_history = exec_history

        def action(self,data):
            return self.exec_history

Contribution
------------
Everyone is welcome to contribute to this project. Source code is available on GitHub.
https://github.com/0x1001/isock

