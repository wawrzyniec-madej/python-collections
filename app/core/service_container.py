from app.exception.service_not_exists_exception import ServiceNotExistsException


class ServiceContainer:
    __services = {}

    def register(self, key: str, element: object) -> None:
        self.__services[key] = element

    def get(self, key: str) -> object:
        if key not in self.__services.keys():
            raise ServiceNotExistsException

        return self.__services[key]
