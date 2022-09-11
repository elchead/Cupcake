import pytest

from cup import *


def test_cupcakename():
    item = Cupcake()

    assert str(item) == "🧁"

# def test_chocolate():
#     item = Chocolate()

#     assert cupcakename(item) == "🍫"

def test_cupcake_with_chocolate_and_peanuts():
    assert str(Peanuts(Chocolate(Cupcake()))) == "🧁 with 🍫 with 🥜"