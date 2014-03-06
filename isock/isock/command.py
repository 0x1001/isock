import SocketServer

################################################################################
################################### Classes ####################################
################################################################################
class ServerException(Exception): pass

class Server(SocketServer.ThreadingTCPServer):
    """
        Socket Server class

        Variables:
    """
