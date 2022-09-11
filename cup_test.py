import pytest

from cup import *


def test_cupcakename():
    item = Cupcake()
    assert str(item) == "🧁"


def test_cupcake_with_chocolate_and_peanuts():
    assert Peanuts(Chocolate(Cupcake())).name() == "🧁 with 🍫 and 🥜"

def test_price():
    Chocolate(Cupcake()).price() == 1.1

    Peanuts(Chocolate(Cupcake())).price() == 1.3