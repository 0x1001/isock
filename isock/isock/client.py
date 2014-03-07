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

        super(Client).__init__()

    def executeAction(action_class,data=None): #???????????????????????????????????????????????????????????????????????????????????????????
        """
            This command executes action on server with given data.

            Input:
            action_class    - Action class
            data            - Data to send to server

            Returns:
            Received data
        """
        raw_data  = self._sendAndReceive(base.BaseData().serlialize((action_class,data)))

        receive_action,receive_data = base.BaseData().deserialize(raw_data)

        if isinstance(receive_action,base.ISockBaseException): raise ClientException(receive_action)

        return receive_data

    def _sendAndReceive(data_to_send):
        """
            This function sends and receives data from server

            Input:
            data_to_send    - data to send

            Returns:
            Received data
        """
        error = None
        for retry in range(self._retry):
            conn.open()
            try:
                conn.connect(self._ip,self._port)
                conn.send(data_to_send)
                data_received = conn.receive()
            except base.ISockBaseException as error:
                continue
            else:
                break
            finally:
                conn.close()
        else:
            raise ClientException("Retry limit exceeded. Error: " + str(error))

        return data_received