from Male import Male
from Female import Female
from Tribes import Tribes
import random
import pickle
import matplotlib.pyplot as plt
import numpy as np

startMen = [
    Male(19,Tribes.BANAKA),
    Male(20,Tribes.KARIMERA),
    Male(23,Tribes.BURUNG),
    Male(25,Tribes.PALYERI),
    Male(18,Tribes.BANAKA),
    Male(22,Tribes.KARIMERA),
    Male(22,Tribes.BURUNG),
    Male(40,Tribes.PALYERI),
]
startWomen = [
    Female(16,Tribes.BANAKA),
    Female(17,Tribes.KARIMERA),
    Female(23,Tribes.BURUNG),
    Female(20,Tribes.PALYERI),
    Female(21,Tribes.BANAKA),
    Female(27,Tribes.KARIMERA),
]

def load_data():
    try:
        with open("inicial_3.pkl", "rb") as file:
            var = pickle.load(file)
    except:
        var = []
    return var

def save_data(data):
    with open("final_1.pkl", "wb") as file:
        pickle.dump(data, file)

#people = load_data()
people = startMen + startWomen

def calculateMarriageCompatibilities(men, women):
    compatibility = []
    for w in women:
        for m in men:
            if w.checkCompatibility(m):
                compatibility.append({"w":w,"m":m,"score":w.checkCompatibility(m)})
    return compatibility

def effectuateMarriages(men, women):
    possibleMarriages = calculateMarriageCompatibilities(men, women)
    possibleMarriages.sort(reverse=True, key = lambda m: m["score"])
    for marriage in possibleMarriages:
        print(marriage)
        m = marriage["m"]
        w = marriage["w"]
        if not w.isMarried() and not m.isMarried():
            m.marry(w)
            w.marry(m)
            men.remove(m)
            women.remove(w)

def effectuatePregnancies(women, time):
    for w in women:
        if w.canBeImpregnated(time):
            w.impregnate(time)
        if w.isDue(time):
            print(w, "had a baby", w.giveBirth())
            people.append(w.giveBirth())

def runSimulation(years):
    months = years*12
    willingToMarryW = []
    willingToMarryM = []
    
    for month in range(int(months)):
        if month % 12 == 0:
            print("Any: ", month/12)
        for person in people:
            if person.alive:
                person.age = person.age + 1/12
                if person.shouldDie():
                    person.die()
                    if person in willingToMarryM:
                        willingToMarryM.remove(person)
                    if person in willingToMarryW:
                        willingToMarryW.remove(person)
                    people.remove(person)
                    continue
                if not person.isMarried() and person not in willingToMarryM and person not in willingToMarryW:
                    if person.shouldMarry():
                        if isinstance(person, Female):
                            willingToMarryW.append(person)
                            print("I want to marry.", person)
                        else:
                            willingToMarryM.append(person)
                            print("I want to marry.", person)
        effectuateMarriages(willingToMarryM, willingToMarryW)
        effectuatePregnancies([p for p in people if isinstance(p, Female) and p.isMarried()], month)

#runSimulation(100)

#save_data(people)

for person in people:
    print(person)

effectuateMarriages(startMen,startWomen)

for person in people:
    print(person)

#print(len(people))

labels = ['0-10','11-20','21-30','31-40','41-50','51-60','61-70','71-80']
banaka = [0, 0, 0, 0, 0, 0, 0, 0]
karimera = [0, 0, 0, 0, 0, 0, 0, 0]
burung = [0, 0, 0, 0, 0, 0, 0, 0]
palyeri = [0, 0, 0, 0, 0, 0, 0, 0]
#clrsBlau = [(0.773,0.804,0.753,0.80), (0.255,0.671,0.643,0.67), (0.384,0.604,0.549,0.60), (0.004,0.412,0.376,0.41)]
clrsMarro = [(0.792,0.694,0.608,0.79), (0.655,0.514,0.412,0.66), (0.651,0.420,0.314,0.65), (0.545,0.337,0.220,0.70)]

for person in people:
    if person.age <= 10:
        if person.tribe == Tribes.BANAKA:
            banaka[0] += 1
        if person.tribe == Tribes.BURUNG:
            burung[0] += 1
        if person.tribe == Tribes.KARIMERA:
            karimera[0] += 1
        if person.tribe == Tribes.PALYERI:
            palyeri[0] += 1
    elif person.age <= 20:
        if person.tribe == Tribes.BANAKA:
            banaka[1] += 1
        if person.tribe == Tribes.BURUNG:
            burung[1] += 1
        if person.tribe == Tribes.KARIMERA:
            karimera[1] += 1
        if person.tribe == Tribes.PALYERI:
            palyeri[1] += 1
    elif person.age <= 30:
        if person.tribe == Tribes.BANAKA:
            banaka[2] += 1
        if person.tribe == Tribes.BURUNG:
            burung[2] += 1
        if person.tribe == Tribes.KARIMERA:
            karimera[2] += 1
        if person.tribe == Tribes.PALYERI:
            palyeri[2] += 1
    elif person.age <= 40:
        if person.tribe == Tribes.BANAKA:
            banaka[3] += 1
        if person.tribe == Tribes.BURUNG:
            burung[3] += 1
        if person.tribe == Tribes.KARIMERA:
            karimera[3] += 1
        if person.tribe == Tribes.PALYERI:
            palyeri[3] += 1
    elif person.age <= 50:
        if person.tribe == Tribes.BANAKA:
            banaka[4] += 1
        if person.tribe == Tribes.BURUNG:
            burung[4] += 1
        if person.tribe == Tribes.KARIMERA:
            karimera[4] += 1
        if person.tribe == Tribes.PALYERI:
            palyeri[4] += 1
    elif person.age <= 60:
        if person.tribe == Tribes.BANAKA:
            banaka[5] += 1
        if person.tribe == Tribes.BURUNG:
            burung[5] += 1
        if person.tribe == Tribes.KARIMERA:
            karimera[5] += 1
        if person.tribe == Tribes.PALYERI:
            palyeri[5] += 1
    elif person.age <= 70:
        if person.tribe == Tribes.BANAKA:
            banaka[6] += 1
        if person.tribe == Tribes.BURUNG:
            burung[6] += 1
        if person.tribe == Tribes.KARIMERA:
            karimera[6] += 1
        if person.tribe == Tribes.PALYERI:
            palyeri[6] += 1
    else:
        if person.tribe == Tribes.BANAKA:
            banaka[7] += 1
        if person.tribe == Tribes.BURUNG:
            burung[7] += 1
        if person.tribe == Tribes.KARIMERA:
            karimera[7] += 1
        if person.tribe == Tribes.PALYERI:
            palyeri[7] += 1

x = np.arange(len(labels))
width = 0.2

fig, ax = plt.subplots()
rects1 = ax.bar(x - 3*width/2, banaka, width, label='Banaka', color = clrsMarro[0])
rects2 = ax.bar(x - width/2, karimera, width, label='Karimera', color = clrsMarro[1])
rects3 = ax.bar(x + width/2, burung, width, label='Burung', color = clrsMarro[2])
rects4 = ax.bar(x + 3*width/2, palyeri, width, label='Palyeri', color = clrsMarro[3])

ax.set_ylabel('Número de persones')
ax.set_xlabel('Edats de les persones')
ax.set_title("Distribució de la societat segons la classe i l'edat")
ax.set_xticks(x, labels)
ax.legend()

fig.tight_layout()

#plt.show()
