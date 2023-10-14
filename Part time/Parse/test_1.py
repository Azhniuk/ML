import pytest
from circuitsitem import CircuitsItem

# positive_id, negative_id, component_value attributes must be >= 0
def test_biggerThanZero_positive_id():
    item = CircuitsItem("Kate", 4, 2, 3)
    assert item.positive_id >= 0
    pass

def test_biggerThanZero_negative_id():
    item = CircuitsItem("Kate", 4, 2, 3)
    assert item.negative_id >= 0
    pass


def test_biggerThanZero_component_value():
    item = CircuitsItem("Kate", 4, 2, 3)
    assert item.component_value >= 0
    pass

# positive_id, negative_id, component_value must be the same type as specified in the annotation
def test_typeCheck_positive_id():
    item = CircuitsItem("Kate", 4, 2, 3)
    assert type(item.positive_id) == int
    pass

def test_typeCheck_negative_id():
    item = CircuitsItem("Kate", 4, 2, 3)
    assert type(item.negative_id) == int
    pass

def test_typeCheck_component_value():
    item = CircuitsItem("Kate", 4, 2, 3)
    assert type(item.component_value) == int or type(item.component_value) == float
    pass

# name must be a string
def test_typeCheck_name():
    item = CircuitsItem("Kate", 4, 2, 3)
    assert type(item.name) == str
    