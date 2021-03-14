size = int(input("Размер массива "))
first = int(input("Первый элемент"))
toplus = int(input("Шаг прогрессии"))
import builtins


def print(mass):
    if len(mass) < 0:
        builtins.print("There is no mass")
        return mass
    if len(mass) == 0:
        builtins.print("[]")
        return mass
    builtins.print("[", mass[0], sep="", end="")
    for i in range(1, len(mass)):
        builtins.print(", ", mass[i], sep="", end="")
    builtins.print("]\n")
    return mass


def create(size, first=0, toplus=0):
    return [first + item * toplus for item in range(size)]


def sort(mass):
    for i in range(1, len(mass)):
        key = mass[i]
        j = i - 1
        while j >= 0 and key < mass[j]:
            mass[j + 1] = mass[j]
            j -= 1
        mass[j + 1] = key
    return mass


print(sort(create(size, first, toplus)))
