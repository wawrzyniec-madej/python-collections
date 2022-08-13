from app.entity.dog import Dog
from app.helper.dog_name_helper import DogNameHelper
from app.value_object.color import Color


class DogFactory:
    def create(self, color: Color) -> Dog:
        return Dog(DogNameHelper.get_dog_name(), color)
