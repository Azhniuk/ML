# Task 3:
# Task: Write your own implementation of the CircuitsItem class to pass the tests from task 2.

from typing import Union
from test_1 import *

class CircuitsItem:
    def __init__(self, name: str, positive_id: int = 0, negative_id: int = 0, component_value: Union[float, int] = 0.0):
        super(CircuitsItem, self).__init__()
        self._name = name
        self._positive_id = positive_id
        self._negative_id = negative_id
        self._component_value = component_value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @property
    def positive_id(self):
        return self._positive_id

    @positive_id.setter
    def positive_id(self, new_index: int):
        self._positive_id = new_index

    @property
    def negative_id(self):
        return self._negative_id

    @negative_id.setter
    def negative_id(self, new_index: int):
        self._negative_id = new_index

    @property
    def component_value(self):
        return self._component_value

    @component_value.setter
    def component_value(self, new_value: Union[float, int]):
        self._component_value = new_value



item = CircuitsItem("Kate", "ff", 2, 3)
