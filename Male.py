from Person import Person
import random

class Male(Person):
    def __init__(self, age, tribe):
        super().__init__(age, tribe)

    def __str__(self) -> str:
        return super().__str__() + "[Male]"

    def __repr__(self) -> str:
        return super().__repr__() + "[Male]"

    def getMarryRate(self):
        if self.age <= 18:
            return 0
        elif self.age <= 25:
            return 0.05
        elif self.age <= 35:
            return 0.03
        elif self.age <= 40:
            return 0.012
        else:
            return 0.0042

    def shouldMarry(self):
        return random.random() <= self.getMarryRate()


