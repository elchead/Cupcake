
class Cupcake:


    def __str__(self) -> str:
        return "cupcake"

class Chocolate:
    def __str__(self) -> str:
        return "chocolate"
    

def cupcakename(item):
    if item == "cupcake":
        return "🧁"

    if item == "chocolate":
        return "🍫"
    