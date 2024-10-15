from functools import total_ordering

@total_ordering
class Animal(object):
    breed: str
    __age: int = 0.0
    _weight: int

    def __repr__(self):
        return f"{self.breed}, {self.__age}, {self._weight}"
    def __str__(self):
        return f"{self.breed}: {self.__age} év, {self._weight} kg."
    def __eq__(self, other):
        if isinstance(other, Animal):
            return isinstance(other, Animal) and other.breed == self.breed and other.__age == self.__age and other._weight == self._weight
    def __lt__(self, other: object) ->bool:
        if not isinstance(other, Animal):
            return NotImplemented
        return self.breed < other.breed and self._weight < other._weight
    def __gt__(self, other: object) ->bool:
        if not isinstance(other, Animal):
            return NotImplemented
        return self.__age > other.__age
    def __init__(self, breed: str, __age: int, _weight: int):
        self.breed = breed
        self.__age = __age
        self._weight = _weight
    def get_age(self):
        return self.__age
    @staticmethod
    def get_age_by_breed(animals: list[object], breed_name) -> list[int]:
        agelst = []
        for animal in animals:
            if  isinstance(animal, Animal) and animal.breed == breed_name:
                agelst.append(animal.get_age())
        return agelst
        #gpt megoldasa
        #return [animal.get_age() for animal in animals if animal.breed == breed_name]
class Mammals(Animal):
    __legs: int

def main() -> None:
    a1 = Animal("Macska", 4, 6)
    a2 = Animal("Kutya", 6, 8)
    a3 = Animal("Macska", 8, 10)
    a4 = Animal("Kutya", 10, 12)
    a5 = Animal("Macska", _weight=10)
    mylist = []
    mylist.append(a1)
    mylist.append(a2)
    mylist.append(a3)
    mylist.append(a4)
    print(Animal.get_age_by_breed(mylist, "Macska"))
    print(a5)
if __name__ == '__main__':
    main()