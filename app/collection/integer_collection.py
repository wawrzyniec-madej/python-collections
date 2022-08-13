from app.collection.abstract_collection import AbstractCollection
from app.exception.invalid_collection_element_type_exception import InvalidCollectionElementTypeException


class IntegerCollection(AbstractCollection):
    def is_duplicate(self, element) -> bool:
        return False

    def validate(self, element) -> None:
        if not isinstance(element, int):
            raise InvalidCollectionElementTypeException()
