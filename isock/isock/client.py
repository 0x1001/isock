import base

################################################################################
################################### Classes ####################################
################################################################################
class ClientException(base.BaseClientException): pass

class Client(base.BaseClient):
    """
        Client class

        Variables:
        _ip             - Server ip
        _port           - Server port
        _retry          - Retry number
    """
    def __init__(self,ip,port,retry=3):
        self._ip = ip
        self._port = port
        self._retry = retry

        super(Client,self).__init__()

    def executeAction(self,action_class,data=None):
        """
            This command executes action on server with given data.

            Input:
            action_class    - Action class
            data            - Data to send to server

            Returns:
            Received data
        """
        import isockdata

        isock_data = isockdata.ISockData()
        isock_data.setActionClass(action_class)
        isock_data.setInputData(data)

        isock_data.from_string(self._sendAndReceive(isock_data.to_string()))

        if isock_data.getException() != None: raise ClientException(isock_data.getException())

        return isock_data.getOutputData()

    def _sendAndReceive(self,data_to_send):
        """
            This function sends and receives data from server

            Input:
            data_to_send    - data to send

            Returns:
            Received data
        """
        error = None
        for retry in range(self._retry):
            self.open()
            try:
                self.connect(self._ip,self._port)
                self.send(data_to_send)
                data_received = self.receive()
            except base.ISockBaseException as error:
                continue
            else:
                break
            finally:
                self.close()
        else:
            raise ClientException("Retry limit exceeded. Error: " + str(error))

        return data_received