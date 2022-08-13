class InvalidColorValueException(Exception):
    __message = 'Color type is invalid'

    def __init__(self):
        super().__init__(self.__message)
