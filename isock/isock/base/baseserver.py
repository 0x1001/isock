import base
import SocketServer

######################################################################################
################################### Classes ##########################################
######################################################################################

class BaseServerException(base.ISockBaseException): pass

class BaseServer(SocketServer.ThreadingTCPServer):
    def __init__(self,address,handler):
        SocketServer.ThreadingTCPServer.__init__(self,address,handler)
