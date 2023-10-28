from Tribes import Tribes
import random
import itertools
import math

class Person:

    newid = itertools.count().__next__

    def __init__(self, age, tribe):
        self.age = age
        self.tribe = tribe
        self.alive = True
        self.marriage = False
        self.partner = None
        self.id = Person.newid()

    def __str__(self) -> str:
        return "#{id}({age}, {tribe})[{status}, {alive}]".format(id=self.id, age=math.trunc(self.age), tribe=self.tribe.value, status="M" if self.isMarried() else "S", alive="A" if self.isAlive() else "D")
     
    def __repr__(self) -> str:
        return "#{id}".format(id=self.id)

    def getDeathRate(self):
        if self.age <= 1:
            return 0.00049
        elif self.age <= 24:
            return 0.000034
        elif self.age <= 54:
            return 0.00045
        elif self.age <= 75:
            return 0.0031
        else:
            return 0.05
        
    def shouldDie(self):
        return random.random() <= self.getDeathRate()

    def die(self):
        self.alive = False
        print("I'm dead.", self)

    def marry(self, partner):
        self.marriage = True
        self.partner = partner
        print("I,", self, ", am married to ", partner)

    def isAlive(self):
        return self.alive

    def isMarried(self):
        return self.marriage
