tops = []
def toppings(constr):
    def wrapper(*args, **kwargs):
        c = constr(*args)
        tops.append(c)
        return c
    return wrapper

class Cupcake:
    components = None
    def __str__(self) -> str:
        return "🧁"

class Chocolate:
    def __init__(self, current):
        if not current.components:
            self.components = []
        else:
            self.components = current.components
        self.components.append(str(current))
        self.components.append("🍫")
        


    def __str__(self) -> str:
        return ' with '.join(self.components)
    
class Peanuts:
    @toppings
    def __init__(self, additional):
        self.base = additional

    def __str__(self) -> str:
        return "🥜"

class Toppings:
    def __init__(self):
        self.ls = []
    
    def appendlist(self, topping):
        self.ls.append(topping)






def cupcakename(item):

    topping = str(item)
    if item.base:
        base = str(item.base)
        return base + " with " + topping

    

    return topping