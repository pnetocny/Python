#Importování knihoven:
import tkinter as tk
from tkinter import messagebox
from tkinter import font

# Funkce pro nakreslení obdelníku:
def draw_rectangle():
    width = float(entry_num1.get()) # šířka obdelníku
    height = float(entry_num2.get()) # výška obdelníku 
    scale = 38  # Poměr 1 cm = 37.7953 pixelů

    canvas.delete("rectangle")  # Vymazat předchozí obdélník

    # Vypočítat souřadnice vrcholů obdélníku
    x1 = 30
    y1 = 30
    x2 = x1 + width * scale
    y2 = y1 + height * scale

    # Nakreslit obdélník
    canvas.create_rectangle(x1, y1, x2, y2, fill="yellow", tags="rectangle")

    # Výpočet obsahu a obvodu obdélníka
    area = width * height
    perimeter = 2 * (width + height)

    # Aktualizovat výstupní text
    area_label.config(text=f"Obsah zadaného obdelníku je: {area} cm2")
    perimeter_label.config(text=f"Obvod zadaného obdelníku je: {perimeter} cm")


# Vytvoření hlavního okna aplikace:
window = tk.Tk()

# Vytvoření názvu okna:
window.title("GUI for Python")

# Nastavení šířky a výšky okna
width = 1300
height = 900
window.geometry(f"{width}x{height}")

# Vytvoření sítě:
cell_00 = tk.Label(window, text="             ."); cell_00.grid(row=0, column=0, sticky="w")
cell_01 = tk.Label(window, text="             ."); cell_01.grid(row=0, column=1, sticky="w")
cell_02 = tk.Label(window, text="             ."); cell_02.grid(row=0, column=2, sticky="w")
cell_03 = tk.Label(window, text="             ."); cell_03.grid(row=0, column=3, sticky="w")
cell_04 = tk.Label(window, text="             ."); cell_04.grid(row=0, column=4, sticky="w")
cell_05 = tk.Label(window, text="             ."); cell_05.grid(row=0, column=5, sticky="w")
cell_06 = tk.Label(window, text="             ."); cell_06.grid(row=0, column=6, sticky="w")
cell_07 = tk.Label(window, text="             ."); cell_07.grid(row=0, column=7, sticky="w")
cell_08 = tk.Label(window, text="             ."); cell_08.grid(row=0, column=8, sticky="w")
cell_09 = tk.Label(window, text="             ."); cell_09.grid(row=0, column=9, sticky="w")
cell_10 = tk.Label(window, text="             ."); cell_10.grid(row=0, column=10, sticky="w")
cell_11 = tk.Label(window, text="             ."); cell_11.grid(row=0, column=11, sticky="w")
cell_12 = tk.Label(window, text="             ."); cell_12.grid(row=0, column=12, sticky="w")
cell_13 = tk.Label(window, text="             ."); cell_13.grid(row=0, column=13, sticky="w")
cell_14 = tk.Label(window, text="             ."); cell_14.grid(row=0, column=14, sticky="w")
cell_15 = tk.Label(window, text="             ."); cell_15.grid(row=0, column=15, sticky="w")
cell_16 = tk.Label(window, text="             ."); cell_16.grid(row=0, column=16, sticky="w")
cell_17 = tk.Label(window, text="             ."); cell_17.grid(row=0, column=17, sticky="w")
cell_18 = tk.Label(window, text="             ."); cell_18.grid(row=0, column=18, sticky="w")
cell_19 = tk.Label(window, text="             ."); cell_19.grid(row=0, column=19, sticky="w")

# Vytvoření vlastního titulku:
title_label = tk.Label(window, text="Nákres a výpočet obsahu a obvodu obdelníku", font=("Helvetica", 14, "bold"))
title_label.grid(row=1, column=1, columnspan=18, sticky="w")

# Prázdný řádek 1
empty_row1 = tk.Label(window, text="", width=10); empty_row1.grid(row=2, column=1, columnspan=19)

# Vytvoření instance písma
title_font = font.Font(family="Helvetica", size=14, weight="normal")
window.option_add("*Font", title_font)

# Vytvoření vstupních polí pro zadání čísel
label_num1 = tk.Label(window, text="Zadej šířku obdelníku:"); label_num1.grid(row=3, column=1, columnspan=6, sticky="w")
entry_num1 = tk.Entry(window); entry_num1.grid(row=3, column=7, columnspan=8, sticky="w")

label_num2 = tk.Label(window, text="Zadej výšku obdelníku:"); label_num2.grid(row=4, column=1, columnspan=6, sticky="w")
entry_num2 = tk.Entry(window); entry_num2.grid(row=4, column=7, columnspan=8, sticky="w")

# Prázdný řádek 2
empty_row2 = tk.Label(window, text="", width=10); empty_row2.grid(row=5, column=1, columnspan=19)

# Tlačítko pro kreslení obdélníku
button_draw = tk.Button(window, text="Nakreslit a vypočítat obsah a obvod", command=draw_rectangle); button_draw.grid(row=6, column=1, columnspan=10, sticky="w")

# Prázdný řádek 3
empty_row2 = tk.Label(window, text="", width=10); empty_row2.grid(row=7, column=1, columnspan=19)

# Výstupní text pro obsah:
area_label = tk.Label(window, text="Obsah zadaného obdelníku je: 0 cm2"); area_label.grid(row=8, column=1, columnspan=19, sticky="w")

# Prázdný řádek 4
empty_row2 = tk.Label(window, text="", width=10); empty_row2.grid(row=9, column=1, columnspan=19)

# Výstupní text pro obvod:
perimeter_label = tk.Label(window, text="Obvod zadaného obdelníku je: 0 cm"); perimeter_label.grid(row=10, column=1, columnspan=19, sticky="w")

# Prázdný řádek 5
empty_row2 = tk.Label(window, text="", width=10); empty_row2.grid(row=11, column=1, columnspan=19)

# Plátno pro kreslení
canvas = tk.Canvas(window, width=1100, height=500, bg="white"); canvas.grid(row=12, column=1, columnspan=19, sticky="nsew")

# Spuštění hlavní smyčky aplikace:
window.mainloop()
