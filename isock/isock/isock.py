################################################################################
################################### Constants ##################################
################################################################################
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

def sendAndReceive(ip,port,data_to_send,retry=3):
    """
        This function sends and receives frames from server

        Input:
        data_to_send    - frame to send

        Returns:
        Received data
    """
    connection = CommClient()
    try:
        connection.connect(ip,port)
        connection.send(data_to_send)
        data_received = connection.receive()
        connection.close()
    except comm.CommException as error:
        if retry == 0: raise CommClientException(error)
        print str(error) + "  Retrying ... " + str(retry)
        retry -= 1
        data_received = sendAndReceive(ip,port,data_to_send,retry)

    return data_received