"""
(From wikipedia)
Duck typing is an application of the duck test ("If it walks like a duck and it quacks like a duck, then it must be a duck")-
to determine if an object can be used for a particular purpose.

With normal typing, suitability is determined by an object's type.
In duck typing, an object's suitability is determined by the presence of certain methods and properties, rather than the type of the object itself.
"""


class Duck:
    def fly(self):
        print("Duck flying")


class Sparrow:
    def fly(self):
        print("Sparrow flying")


class Whale:
    def swim(self):
        print("Whale swimming")


def main():
    for animal in Duck(), Sparrow(), Whale():
        try:
            animal.fly()
        except AttributeError:
            print(f"Animal '{type(animal).__name__}' cannot fly")


if __name__ == "__main__":
    main()

"""
output:
-------
Duck flying
Sparrow flying
Animal 'Whale' cannot fly
"""
