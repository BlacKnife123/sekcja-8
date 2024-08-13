generatorLiczb = (
    number
    for number in range(100,471)
    if number % 7 == 0 and number % 5 != 0
)


wyrazenie_listowe = [
    number
    for number in range(100,471)
    if number % 7 == 0 and number % 5 != 0
]

print(generatorLiczb)
print(wyrazenie_listowe)
