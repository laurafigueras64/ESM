from Person import Person
from Male import Male
import random

from Tribes import Tribes

class Female(Person):
    def __init__(self, age, tribe):
        super().__init__(age, tribe)
        self.pregnant = False
        self.lastPregnantTime = -12

    def __str__(self) -> str:
        return super().__str__() + "[Female]"

    def __repr__(self) -> str:
        return super().__repr__() + "[Female]"

    def getMarryRate(self):
        if self.age <= 16:
            return 0
        elif self.age <= 20:
            return 0.046
        elif self.age <= 25:
            return 0.025
        elif self.age <= 35:
            return 0.012
        else:
            return 0.0042

    def shouldMarry(self):
        return random.random() <= self.getMarryRate()

    def checkCompatibility(self, male):
        if self.tribe == Tribes.BANAKA:
            if male.tribe != Tribes.BURUNG:
                return 0
        elif self.tribe == Tribes.KARIMERA:
            if male.tribe != Tribes.PALYERI:
                return 0
        elif self.tribe == Tribes.BURUNG:
            if male.tribe != Tribes.BANAKA:
                return 0
        elif self.tribe == Tribes.PALYERI:
            if male.tribe != Tribes.KARIMERA:
                return 0
        if self.age > male.age+5:
            return 0
        elif self.age < male.age-10:
            return 0
        else:
            return 1/(1+(male.age-self.age-3)*(male.age-self.age-3))

    def getBirthRate(self):
        if self.age <= 25:
            return 0.028
        elif self.age <= 35:
            return 0.012
        elif self.age <= 40:
            return 0.0026
        elif self.age <= 45:
            return 0.00005
        else:
            return 0

    def shouldImpregnate(self): 
        return random.random() <= self.getBirthRate()

    def canBeImpregnated(self, time):
        return self.isMarried() and self.partner.isAlive() and time - self.lastPregnantTime >= 12 and self.shouldImpregnate()

    def impregnate(self, month):
        self.pregnant = True
        self.lastPregnantTime = month

    def isPregnant(self):
        return self.pregnant

    def isDue(self, time):
        return self.isPregnant() and time - self.lastPregnantTime >= 9

    def giveBirth(self):
        self.pregnant = False
        if self.tribe == Tribes.BANAKA:
            if random.random() < 0.5:
                return Male(0, Tribes.KARIMERA)
            else:
                return Female(0, Tribes.KARIMERA)
        if self.tribe == Tribes.BANAKA:
            if random.random() < 0.5:
                return Male(0, Tribes.KARIMERA)
            else:
                return Female(0, Tribes.KARIMERA)
        elif self.tribe == Tribes.KARIMERA:
            if random.random() < 0.5:
                return Male(0, Tribes.BANAKA)
            else:
                return Female(0, Tribes.BANAKA)  
        elif self.tribe == Tribes.BURUNG:
            if random.random() < 0.5:
                return Male(0, Tribes.PALYERI)
            else:
                return Female(0, Tribes.PALYERI)
        elif self.tribe == Tribes.PALYERI:
            if random.random() < 0.5:
                return Male(0, Tribes.BURUNG)
            else:
                return Female(0, Tribes.BURUNG)    


