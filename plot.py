from Tribes import Tribes
import engine
import matplotlib.pyplot as plt
import numpy as np
import pickle

def load_data():
    try:
        with open("finalResult.pkl", "rb") as file:
            var = pickle.load(file)
    except:
        var = []
    return var

people = load_data()

for person in people:
    print(person)

labels = ['0-10','11-20','21-30','31-40','41-50','51-60','61-70','71-80']
banaka = [0, 0, 0, 0, 0, 0, 0, 0]
karimera = [0, 0, 0, 0, 0, 0, 0, 0]
burung = [0, 0, 0, 0, 0, 0, 0, 0]
palyeri = [0, 0, 0, 0, 0, 0, 0, 0]

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
rects1 = ax.bar(x - 3*width/2, banaka, width, label='Banaka')
rects2 = ax.bar(x - width/2, karimera, width, label='Karimera')
rects3 = ax.bar(x + width/2, burung, width, label='Burung')
rects4 = ax.bar(x + 3*width/2, palyeri, width, label='Palyeri')

ax.set_ylabel('Número de persones')
ax.set_xlabel('Edats de les persones')
ax.set_title("Distribució de la societat segons la classe i l'edat")
ax.set_xticks(x, labels)
ax.legend()

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)
#ax.bar_label(rects3, padding=3)
#ax.bar_label(rects4, padding=3)

fig.tight_layout()

plt.show()
