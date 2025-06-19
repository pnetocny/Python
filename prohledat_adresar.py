import os
import PyPDF2
from datetime import datetime

def najdi_pocet_podpisu(cesta_k_souboru):
    try:
        with open(cesta_k_souboru, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            root = reader.trailer["/Root"]

            if "/AcroForm" in root:
                acroform = root["/AcroForm"]
                if "/Fields" in acroform:
                    fields = acroform["/Fields"]
                    pocet_podpisu = 0
                    for field in fields:
                        field_obj = field.get_object()
                        if field_obj.get("/FT") == "/Sig":
                            if "/V" in field_obj:
                                pocet_podpisu += 1
                    return pocet_podpisu
            return 0
    except Exception as e:
        print(f"Chyba při čtení souboru {cesta_k_souboru}: {e}")
        return 0

# Nastavení cesty k adresáři
adresar = input("Zadej cestu k adresáři s PDF soubory: ")

# Najdeme všechny PDF soubory
pdf_soubory = [soubor for soubor in os.listdir(adresar) if soubor.lower().endswith('.pdf')]

# Zjistíme celkový počet souborů
celkovy_pocet = len(pdf_soubory)

# Slovníky pro seskupení souborů
bez_podpisu = []
s_jednim_podpisem = []
s_vice_podpisy = []

# Analyzujeme každý soubor
for soubor in pdf_soubory:
    cesta_k_souboru = os.path.join(adresar, soubor)
    pocet_podpisu = najdi_pocet_podpisu(cesta_k_souboru)
    
    if pocet_podpisu == 0:
        bez_podpisu.append(soubor)
    elif pocet_podpisu == 1:
        s_jednim_podpisem.append(soubor)
    else:
        s_vice_podpisy.append(soubor)

# Mezivýpočty
pocet_bez_podpisu = len(bez_podpisu)
pocet_s_jednim_podpisem = len(s_jednim_podpisem)
pocet_s_vice_podpisy = len(s_vice_podpisy)

# Vypíšeme výsledky
print(f"\nCelkový počet zkontrolovaných PDF souborů: {celkovy_pocet}\n")

print(f"0 podpisů: {pocet_bez_podpisu}")
for soubor in bez_podpisu:
    print(f"- {soubor}")

print(f"\n1 podpis: {pocet_s_jednim_podpisem}")
for soubor in s_jednim_podpisem:
    print(f"- {soubor}")

print(f"\n2 a více podpisů: {pocet_s_vice_podpisy}")
for soubor in s_vice_podpisy:
    print(f"- {soubor}")

# Vytvoření názvu výstupního souboru s datem a časem
casovy_stamp = datetime.now().strftime("%Y-%m-%d-%H-%M")
nazev_vystupniho_souboru = f"Vysledek_podpisy_{casovy_stamp}.txt"
cesta_vystupniho_souboru = os.path.join(adresar, nazev_vystupniho_souboru)

# Uložíme výsledky do souboru
with open(cesta_vystupniho_souboru, "w", encoding="utf-8") as f:
    f.write(f"Celkový počet zkontrolovaných PDF souborů: {celkovy_pocet}\n\n")
    f.write(f"0 podpisů: {pocet_bez_podpisu}\n")
    for soubor in bez_podpisu:
        f.write(f"- {soubor}\n")
    f.write(f"\n1 podpis: {pocet_s_jednim_podpisem}\n")
    for soubor in s_jednim_podpisem:
        f.write(f"- {soubor}\n")
    f.write(f"\n2 a více podpisů: {pocet_s_vice_podpisy}\n")
    for soubor in s_vice_podpisy:
        f.write(f"- {soubor}\n")

print(f"\nVýsledky byly uloženy do souboru: {nazev_vystupniho_souboru}")
