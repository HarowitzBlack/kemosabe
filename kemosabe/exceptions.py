

class EventNotFoundError(Exception):
    """ Raise when certain events are not found.
    """
    pass

class ConfigFileNotFound(Exception):
    pass

class KeysNotFound(Exception):
    pass

class InternalError(Exception):
    pass
