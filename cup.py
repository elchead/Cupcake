
class Cupcake:
    def __str__(self) -> str:
        return "cupcake"

class Chocolate:
    def __init__(self, bakery):
        pass

    def __str__(self) -> str:
        return "chocolate"
    

def cupcakename(item):
    item = str(item)
    if item == "cupcake":
        return "🧁"

    if item == "chocolate":
        return "🍫"
    