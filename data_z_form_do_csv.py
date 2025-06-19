import os
import csv
from datetime import datetime
from PyPDF2 import PdfReader

# 🛠️ Funkce: Rozhodni, zda pole má být zahrnuto
def is_valid_field(name):
    return not (name.startswith("Sig") or name.startswith("Signature") or name.startswith("Adobe"))

# 📁 Zadání adresáře od uživatele
adresar = input("Zadej název adresáře s PDF formuláři: ")

# 📄 Vyhledání všech PDF souborů
pdf_soubory = [f for f in os.listdir(adresar) if f.lower().endswith(".pdf")]

# 📅 Vytvoření názvu výstupního souboru s časovým kódem
casovy_kod = datetime.now().strftime("%Y%m%d%H%M")
nazev_csv = f"Data_z_formularu_{casovy_kod}.csv"
cesta_csv = os.path.join(adresar, nazev_csv)

zaznamy = []

# 🔍 Načti pole z každého PDF a ulož jen validní
for soubor in pdf_soubory:
    cesta = os.path.join(adresar, soubor)
    reader = PdfReader(cesta)
    fields = reader.get_fields()
    if fields:
        data = {
            k: v.get('/V', '') for k, v in fields.items() if is_valid_field(k)
        }
        data["__soubor__"] = soubor  # Pomocné pole pro identifikaci
        zaznamy.append(data)

# 📌 Získání všech názvů sloupců
vsechny_pole = sorted({k for z in zaznamy for k in z.keys()})

# 💾 Uložení do CSV
with open(cesta_csv, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=vsechny_pole, delimiter=';')
    writer.writeheader()
    for z in zaznamy:
        writer.writerow(z)

print(f"✅ Hotovo! Data uložena jako: {cesta_csv}")
