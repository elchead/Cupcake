import pytest

from cup import *


def test_cupcakename():
    item = Cupcake()

    assert cupcakename(item) == "🧁"

def test_chocolate():
    item = Chocolate()

    assert cupcakename(str(item)) == "🍫"