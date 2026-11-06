import random

# ad 1) provede načtení řádků do seznamu
def nactiRadky(soubor):
    with open(soubor, "r", encoding="utf-8") as f:
        radky_textu = f.readlines() # ad 2)

    # ad 3 a)
    if not radky_textu:
        print("Soubor neobsahuje žádné řádky.")

    return radky_textu


def mixujRadky(radky):
    # generování seznamu náhodných čísel v rozsahu řádků textu
    uni_cisla = random.sample(range(len(radky)), len(radky))

    index_uni_cisla = 0 #priprava indexu pro iteraci v uni_cisla -> přiřazování hodnoty jako nového indexu řádku
    mix_radku = list(range(len(radky))) # příprava proměnné pro uložení řádku na nové místo, musí být naplněn, aby se dalo místo určit

    for radek in radky:
        mix_radku[uni_cisla[index_uni_cisla]] = radek # umístění řádku na nové místo v seznamu
        index_uni_cisla +=1

    return mix_radku

def ulozRadky(data_k_ulozeni, nazev_souboru):
    with open(nazev_souboru, "w", encoding="utf-8") as f:
        for radek in data_k_ulozeni:
            f.write(radek)
    print(f"Soubor: {nazev_souboru} byl uložen.")





