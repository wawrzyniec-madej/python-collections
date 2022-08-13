from abc import abstractmethod, ABC


class AbstractCollection(ABC):
    _elements: list

    def __init__(self, elements=None):
        if elements is None:
            elements = []

        self._elements = []

        for element in elements:
            self.add(element)

    @abstractmethod
    def validate(self, element) -> None:
        pass

    @abstractmethod
    def is_duplicate(self, element) -> bool:
        pass

    def add(self, element):
        self.validate(element)
        if not self.is_duplicate(element):
            self._elements.append(element)

    def __iter__(self):
        return self._elements.__iter__()
