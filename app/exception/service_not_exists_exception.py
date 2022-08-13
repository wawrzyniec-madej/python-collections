class ServiceNotExistsException(Exception):
    __message = 'Service not exists'

    def __init__(self):
        super().__init__(self.__message)
