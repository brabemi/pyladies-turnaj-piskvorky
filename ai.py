import random

def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    return pole[:cislo_policka] + symbol + pole[int(cislo_policka) + 1:]

def tah_pocitace(pole, symbol):
    if '-' not in pole:
        raise ValueError('Plné pole')
    while True:
        cislo = random.randrange(len(pole))
        if pole[cislo] == '-':
            return pole[:cislo] + symbol + pole[cislo+1:]
