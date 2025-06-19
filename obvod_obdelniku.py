# Výpočet obvodu obdélníku na základě jeho délky a šířky

def obvod_obdelniku(delka, sirka):
    """
    Vypočítá obvod obdélníku.

    Parametry:
        delka (float): Délka obdélníku.
        sirka (float): Šířka obdélníku.

    Návratová hodnota:
        float: Obvod obdélníku.
    """
    return 2 * (delka + sirka)

def nacti_float_kladne(vyzva):
    """
    Načte od uživatele číslo typu float větší než nula.
    Parametry:
        vyzva (str): Textová výzva zobrazená uživateli při zadávání hodnoty.
    Návratová hodnota:
        float: Kladné číslo větší než nula zadané uživatelem.
    Funkce opakovaně žádá uživatele o zadání hodnoty, dokud nezadá platné číslo větší než nula.
    Pokud je zadán neplatný, záporný nebo nulový vstup, zobrazí se chybová hláška a výzva k opětovnému zadání.
    """
    while True:
        try:
            hodnota = float(input(vyzva))
            if hodnota <= 0:
                print("Zadej prosím číslo větší než nula.")
                continue
            return hodnota
        except ValueError:
            print("Zadal jsi neplatné číslo.")


def main():
    # Hlavní funkce pro interakci s uživatelem
    # Načtení délky a šířky obdélníku od uživatele (pouze kladná čísla)
    delka = nacti_float_kladne("Zadej délku obdélníku: ")
    sirka = nacti_float_kladne("Zadej šířku obdélníku: ")
    # Výpočet a výpis výsledku
    vysledek = obvod_obdelniku(delka, sirka)
    print(f"Obvod obdélníku je: {vysledek}")

if __name__ == "__main__":
    # Tento blok se spustí pouze při přímém spuštění souboru, ne při importu jako modul
    main()
