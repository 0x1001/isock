import base

################################################################################
################################### Classes ####################################
################################################################################
class ServerException(base.BaseServerException): pass

class Server(base.BaseServer):
    """
        Socket Server class

        Variables:
        _actions        - List of actions that client can invoke
    """
    def __init__(self,*args,**kargs):
        import threading

        self._actions = []

        super(Server).__init__(*args,**kargs)

    def registerAction(self,action):
        """
            Reqisters server action

            Input:
            action      - Action that client can perform

            Returns:
            Nothing
        """
        try: findAction(type(action))
        except ServerException: self._actions.append(action)
        else:
            raise ServerException("Action is already registered. " + str(type(action)))

    def findAction(self,action_class):
        """
            This function finds and returns action that is an instance of action_class

            Input:
            action_class        - Action class

            Retruns:
            action              - Action object
        """
        for action in self._actions:
            if type(action) == action_class: return action
        else:
            raise ServerException("Cannot find action: " + str(action_class))


class ServerHandler(base.BaseRequestHandler):
    """
        Socket Server handler class

        Variables:
    """

    def handle(self):
        """
            Handles all clients requests

            Input:
            Nothing

            Returns:
            Nothing
        """
        import protocol

        try: received_data = self.receive()
        except base.ISockBaseException as error: pass #TODO



        try: self.send(received_data)
        except base.ISockBaseException as error: pass #TODO