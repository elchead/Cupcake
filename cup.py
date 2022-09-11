class Topping:
    def __init__(self,new,old) -> None:
        self.new = new
        self.old = old

    def __str__(self) -> str:
        return str(self.old)+' with '+str(self.new)


class Cupcake():
    def __str__(self) -> str:
        return "🧁"

    def add(other):
        return [other]

def Chocolate(cake):
    return Topping(_Chocolate(),cake)

class _Chocolate():
    def __str__(self) -> str:
        return "🍫"

def Peanuts(cake):
    return Topping(_Peanuts(),cake)

class _Peanuts:
    def __str__(self) -> str:
        return "🥜"
