"""
Program načte text se souboru, náhodně prohází a vypíše pořadí řádek
Postup:
1. fce na otevření souboru
    a) Try na existenci souboru
2) práce s řádky -> iterace řádků -> readlines
3) fce. promíchání řádků -> změnit index řádků -> vygenerovat seznam náhodných čísel v rozsahu (len)
počtů řádků. Unikátní hodnoty vyřešeny naplněním množiny. Má randomint argument pro unikátní hodnoty?
- vhodné z množiny udělat iterátor
- každému řádku přiřadit číslo z množiny -> proměnná získaná z enumerate
-následně
    a) ošetření neexistence řádků
"""

from utils import nactiRadky, mixujRadky, ulozRadky
import sys

print("""
Program načte text se souboru, náhodně prohází a vypíše pořadí řádek
====================================================================
""")

vstupni_textovy_soubor = input("Zadej umístění vstupního souboru:\n")
promichane_radky_soubor = input("Zadej umístění výstupního souboru:\n")

# ad 1 a)
try:
    nactene_radky = nactiRadky(vstupni_textovy_soubor)
    # ad 3 a)
    if not nactene_radky:
        print("Soubor neobsahuje žádné řádky a není co míchat. Program bude ukončen.")
        sys.exit()

except Exception as e:
    print(f"Načtení souboru se nezdařilo! Nastala chyba: {e}") # můžu rozlišit neexistenci souboru a neexistenci řádků(zřejmě jen prázdný seznam)?
    sys.exit()


try:
    ulozRadky(mixujRadky(nactene_radky), promichane_radky_soubor)
except Exception as e:
    print(f"Soubor se nepodařilo uložit. Nastala chyba: {e}")
