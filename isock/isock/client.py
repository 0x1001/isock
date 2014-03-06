import base

################################################################################
################################### Classes ####################################
################################################################################
class ClientException(base.BaseClientException): pass

class Client(base.BaseClient):
    """
        Client class

        Variables:
    """

    def executeAction(action_class,data=None):
        """
            This command executes action on server with given data.

            Input:
            action_class    - Action class
            data            - Data to send to server

            Returns:
            Received data
        """


    def _sendAndReceive(ip,port,data_to_send,retry=3):
        """
            This function sends and receives data from server

            Input:
            data_to_send    - data to send

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