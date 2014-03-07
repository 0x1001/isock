import base
################################################################################
############################# Classes ##########################################
################################################################################
class ProtocolException(base.ISockBaseException): pass

################################################################################
############################ Functions  ########################################
################################################################################
def serialize(data):
    """
        This function creates protocol frame

        Input:
        data    - Data to serialize

        Returns:
        serialized data
    """
    import cPickle
    return cPickle.dumps(data)

def deserialize(data):
    """
        This function analyzes protocol frame

        Input:
        data        - Serialized data

        Retruns:
        deserialized data
    """
    import cPickle
    return cPickle.loads(data)
