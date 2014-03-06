import base
import SocketServer

######################################################################################
################################### Classes ##########################################
######################################################################################

class BaseServerException(base.ISockBaseException): pass
class BaseServer(SocketServer.ThreadingTCPServer): pass
