class Combo:
    def __init__(self,new,old) -> None:
        self.new = new
        self.old = old

    def __str__(self) -> str:
        return str(self.old)+' with '+str(self.new)

    def price(self):
        return self.old.price() + self.new.price()

    def name(self):
        return replace_last_with_with_and(str(self))


class Cupcake():
    def __str__(self) -> str:
        return "🧁"

    def price(self):
        return 1


def Chocolate(cake):
    return Combo(_Chocolate(),cake)
class _Chocolate():
    def __str__(self) -> str:
        return "🍫"

    def price(self):
        return .1

def Peanuts(cake):
    return Combo(_Peanuts(),cake)
class _Peanuts:
    def __str__(self) -> str:
        return "🥜"

    def price(self):
        return .2

def replace_last_with_with_and(s):
    li = s.rsplit('with', 1)
    return 'and'.join(li)