class InvalidCollectionElementTypeException(Exception):
    __message = 'Collection element type is invalid'

    def __init__(self):
        super().__init__(self.__message)
