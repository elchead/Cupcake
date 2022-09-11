import pytest

from cup import *


def test_cupcakename():
    item = Cupcake()

    assert str(item) == "🧁"

# def test_chocolate():
#     item = Chocolate()

#     assert cupcakename(item) == "🍫"

def test_cupcakewithchocolate():

    assert str(Chocolate(Cupcake())) == "🧁 with 🍫"

# def test_cupcakewithchocandpean():

#     assert cupcakename(Peanuts(Chocolate(Cupcake()))) == "🧁 with 🍫 and 🥜"