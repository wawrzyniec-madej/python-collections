from app.core.service_container import ServiceContainer
from app.service.cat_service import CatService
from app.service.dog_service import DogService


class Kernel:
    __service_container: ServiceContainer

    def __init__(self) -> None:
        self.__service_container = ServiceContainer()

        self.__service_container.register('app.service.dog', DogService())
        self.__service_container.register('app.service.cat', CatService())

        self.__start()

    def __start(self):
        dog_service = self.__service_container.get('app.service.dog')

        dog_service.start()
