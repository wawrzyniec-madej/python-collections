from __future__ import annotations

from app.value_object.color import Color


class Dog:
    __name: str
    __color: Color

    def __init__(self, name: str, color: Color):
        self.__name = name
        self.__color = color

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> Dog:
        self.__name = name
        return self

    def get_color(self) -> Color:
        return self.__color

    def set_color(self, color: Color) -> Dog:
        self.__color = color
        return self
