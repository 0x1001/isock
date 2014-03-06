################################################################################
################################### Constants ##################################
################################################################################
VERSION = "1.0.0"
















REQUEST_QUEUE_SIZE = 10

################################################################################
################################### Functions ##################################
################################################################################

def server_factory(ip,port,request_handler,socket_server=None):
    """
        Prepares Socket server

        Input:
        ip                  - Server address
        port                - Server port
        request_handler     - Request handler function
        socket_server       - Custom Socket server class

        Returns:
        Server handle
    """
    import socket
    import SocketServer

    class Handler(CommServer): handle = request_handler

    socket_server = socket_server if socket_server else SocketServer.ThreadingTCPServer

    socket_server.request_queue_size=3
    try:
        server_handle = socket_server((ip,port),Handler)
    except socket.error as error:
        raise CommServerException(str(error))

    return server_handle
