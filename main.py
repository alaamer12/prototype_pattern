import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype(Prototype):
    def __init__(self, property1, property2):
        self.property1 = property1
        self.property2 = property2

    def __str__(self):
        return f"Property 1: {self.property1}, Property 2: {self.property2}"

if __name__ == "__main__":
    prototype = ConcretePrototype("abc", 123)
    print(f"Original Prototype: {prototype}")

    # Clone the prototype
    cloned_prototype = prototype.clone()
    print(f"Cloned Prototype: {cloned_prototype}")
