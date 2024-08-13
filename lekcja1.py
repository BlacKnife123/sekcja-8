liczby = [1,2,3,4,5,6]

potegiDwojki =[]
for element in liczby:
    potegiDwojki.append(element**2)

potegiDwojki2 = [element**2 for element in liczby]

print(potegiDwojki2)

#--------------------------------------------------------
liczbyParzyste = []
for element in liczby:
    if element % 2 == 0:
        liczbyParzyste.append(element)

liczbyParzyste2 = [element for element in liczby if element % 2 == 0]

print(liczbyParzyste2)

