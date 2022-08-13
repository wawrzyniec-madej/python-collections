from app.exception.invalid_color_value_exception import InvalidColorValueException


class Color:
    red: str = 'red'
    green: str = 'green'

    __available_colors: set = {red, green}
    __value: str

    def __init__(self, value):
        if value not in self.__available_colors:
            raise InvalidColorValueException

        self.__value = value

    def get_value(self) -> str:
        return self.__value
