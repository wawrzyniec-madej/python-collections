from app.collection.abstract_collection import AbstractCollection
from app.entity.dog import Dog
from app.exception.invalid_collection_element_type_exception import InvalidCollectionElementTypeException


class DogCollection(AbstractCollection):
    def validate(self, element) -> None:
        if not isinstance(element, Dog):
            raise InvalidCollectionElementTypeException

    def is_duplicate(self, element) -> bool:
        return element in self._elements
