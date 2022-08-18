class Clothing:
    """
    >>> blue_shirt = Clothing("shirt", "blue")
    >>> blue_shirt.category
    'shirt'
    >>> blue_shirt.color
    'blue'
    >>> blue_shirt.is_clean
    True
    >>> blue_shirt.wear()
    >>> blue_shirt.is_clean
    False
    >>> blue_shirt.clean()
    >>> blue_shirt.is_clean
    True
    """

    def __init__(self, category, color):
        self.category = category
        self.color = color
        self.is_clean = True

    def wear(self):
        self.is_clean = False

    def clean(self):
        self.is_clean = True


class KidsClothing(Clothing):
    """
    >>> onesie = KidsClothing("onesie", "polka dots")
    >>> onesie.wear()
    >>> onesie.is_clean
    False
    >>> onesie.clean()
    >>> onesie.is_clean
    False
    >>> dress = KidsClothing("dress", "rainbow")
    >>> dress.clean()
    >>> dress.is_clean
    True
    >>> dress.wear()
    >>> dress.is_clean
    False
    >>> dress.clean()
    >>> dress.is_clean
    False
    """
  
    # Override the clean() method
    # so that kids clothing always stays dirty!
    def clean(self):
      self.is_clean = self.is_clean

class Parent:
    def f(s):
        print("Parent.f")

    def g(s):
        s.f()

class Child(Parent):
    def f(me):
        print("Child.f")


class Lamb:
    species_name = "Lamb"
    scientific_name = "Ovis aries"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Lamb named " + self.name

    def __repr__(self):
        return f"Lamb({repr(self.name)})"

def number_factor(n):
    """print all the factors of n provided that they are larger than 1"""
    for i in range(2, n):
        if n%i == 0:
            print(i)