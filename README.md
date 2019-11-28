# Turnaj - piškvorky

## Instalace
Aktivujte virtuální prostředí. Nainstalujte závisloti pomocí příkazu `python -m pip install -r requirements.txt`

## Testování
Do souboru `ai.py` vložte funci `def tah_pocitace(pole, symbol):` a další pomocné fukce, které tati funkce potřebuje.
```
def tah_pocitace(pole, symbol):
    ...
    return pole
```
Následně spusťte testy pomocí `pytest -vs test_ai.py`.
Pokud vše funguje. Výstup by měl vypadat takto.
```
========================= test session starts =========================
platform linux -- Python 3.7.5, pytest-5.3.1, py-1.8.0, pluggy-0.13.1 -- /home/brabemi/Documents/pyladies/2019_2/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/brabemi/Documents/pyladies/2019_2/turnaj
collected 8 items

test_ai.py::test_empty PASSED
test_ai.py::test_full PASSED
test_ai.py::test_short PASSED
test_ai.py::test_long PASSED
test_ai.py::test_zero PASSED
test_ai.py::test_almost_full PASSED
test_ai.py::test_almost_full_beginning PASSED
test_ai.py::test_almost_full_end PASSED

========================= 8 passed in 0.02s =========================
```
## Turnaj

Soubor zkopírujte do složky `strategie` a přejmenujte ho na `jmeno_prijmeni.py` (soubor `nahoda.py` ve složce nechte. Turnaj vyzkoušíte příkazem `python turnaj.py`
```
================================================================================
Účastnice:
    mirek_nahoda
    nahoda
================================================================================
Testy:
    0: Hra na prázdné pole
    1: Hra na plné pole
    2: Hra na krátké pole
    3: Hra na dlouhé pole
    4: Hra na pole nulové délky
    5: Hra na skoro plné pole (volno uprostřed)
    6: Hra na skoro plné pole (volno na začátku)
    7: Hra na skoro plné pole (2× volno na konci)

                     0 1 2 3 4 5 6 7
        mirek_nahoda . . . . . . . .
              nahoda . . . . . . . .
--------------------------------------------------------------------------------
================================================================================
Turnáááj!
--------------------------------------------------------------------------------

mirek_nahoda (x) vs. mirek_nahoda (o)
       0 --------------------
       1 ---------x----------
       2 ---o-----x----------
       3 ---o-----xx---------
       4 ---o--o--xx---------
       5 ---o--o--xx---x-----
       6 o--o--o--xx---x-----
       7 o--o--o--xx--xx-----
       8 o--o-oo--xx--xx-----
       9 o--o-oo--xx-xxx-----
    mirek_nahoda vyhrála; +1 bod

mirek_nahoda (x) vs. nahoda (o)
       0 --------------------
       1 ----------------x---
       2 ----------------x--o
       3 ----------x-----x--o
       4 -------o--x-----x--o
       5 -------o--x--x--x--o
       6 -------o--x--xo-x--o
       7 x------o--x--xo-x--o
       8 x--o---o--x--xo-x--o
       9 x--o---o--x-xxo-x--o
      10 x--o--oo--x-xxo-x--o
      11 x--o--oox-x-xxo-x--o
      12 x--o--ooxox-xxo-x--o
      13 x-xo--ooxox-xxo-x--o
      14 x-xoo-ooxox-xxo-x--o
      15 xxxoo-ooxox-xxo-x--o
    mirek_nahoda vyhrála; +1 bod

nahoda (x) vs. mirek_nahoda (o)
       0 --------------------
       1 ----------x---------
       2 -o--------x---------
       3 -o--------x---x-----
       4 -o--o-----x---x-----
       5 -o--o-----x-x-x-----
       6 -o--o-----x-x-x---o-
       7 -o--o-----x-xxx---o-
    nahoda vyhrála; +1 bod

nahoda (x) vs. nahoda (o)
       0 --------------------
       1 ----------x---------
       2 ------o---x---------
       3 ------ox--x---------
       4 ---o--ox--x---------
       5 ---o--ox--xx--------
       6 ---o--ox-oxx--------
       7 ---o--ox-oxx-------x
       8 ---oo-ox-oxx-------x
       9 --xoo-ox-oxx-------x
      10 --xoo-ox-oxx--o----x
      11 --xoo-ox-oxx-xo----x
      12 o-xoo-ox-oxx-xo----x
      13 o-xoo-ox-oxx-xo--x-x
      14 o-xoo-ox-oxx-xo--xox
      15 o-xoo-ox-oxx-xox-xox
      16 ooxoo-ox-oxx-xox-xox
      17 ooxoo-ox-oxx-xoxxxox
    nahoda vyhrála; +1 bod

Pořadí po 1. kole turnaje
                      mirek nahod  Celkem
        mirek_nahoda:   1.0   1.0     2.0 🏆 1. místo
              nahoda:   1.0   1.0     2.0 🏆 2. místo
```
## Poznámky
Vyzkoušejte že strategie:
* umí hrát se symbolem, který dostane
* umí zahrát první tah
* vrací `ValueError` pokud je pole plné
* porazí náhodnou strategii :)
