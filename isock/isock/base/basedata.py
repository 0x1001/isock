import base
################################################################################
############################# Classes ##########################################
################################################################################
class BaseDataException(base.ISockBaseException): pass

################################################################################
############################ Functions  ########################################
################################################################################

class BaseData(object):
    """
        Encoding and decondig class for data transfer

        Variables:
    """
    def serialize(self,data):
        """
            This function creates protocol frame

            Input:
            data    - Data to serialize

            Returns:
            serialized data
        """
        import cPickle

        try: return cPickle.dumps(data)
        except cPickle.PicklingError as error: raise BaseDataException(error)

    def deserialize(self,data):
        """
            This function analyzes protocol frame

            Input:
            data        - Serialized data

            Retruns:
            deserialized data
        """
        import cPickle

        try: return cPickle.loads(data)
        except cPickle.UnpicklingError as error: raise BaseDataException(error)
