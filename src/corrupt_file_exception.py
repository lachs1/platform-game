class CorruptedMapFileError(Exception):

    def __init__(self, message):
        super(CorruptedMapFileError, self).__init__(message)