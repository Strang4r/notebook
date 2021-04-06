from abc import ABC, abstractmethod


class Clothes(ABC):
    @staticmethod
    def all_count(list_of_cloth):
        return sum(piece.consumption for piece in list_of_cloth)

    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def consumption(self):
        print(f'To be consumed for make a coat - {round(self.height / 6.5) + 0.5}')
        return round(self.height / 6.5) + 0.5


class Costume(Clothes):
    def __init__(self, val):
        self.val = val

    @property
    def consumption(self):
        print(f'To be consumed for make a costume - {round(2 * self.val + 0.3) / 0.5}')
        return round(2 * self.val + 0.3) / 0.5


c0 = Coat(25)
c1 = Coat(45)
cos = Costume(60)
clo = [c0, c1, cos]
print(Clothes.all_count(clo))
