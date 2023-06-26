# GUI - Použití kontejneru Grid

#Importování knihoven:
import tkinter as tk
from tkinter import messagebox
from tkinter import font



# Funkce pro provedení operace se zadanými čísly:
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = combo_operation.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                entry_result.delete(0, tk.END)
                entry_result.insert(tk.END, "Nelze dělit nulou!")
                return

        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, result)

    except ValueError:
        entry_result.delete(0, tk.END)
        entry_result.insert(tk.END, "Zadávejte pouze čísla!")

""" Výsledek jde do message boxu:
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = combo_operation.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Chyba", "Nelze dělit nulou!")
                return

        messagebox.showinfo("Výsledek", f"Výsledek: {result}")

    except ValueError:
        messagebox.showerror("Chyba", "Zadávejte pouze čísla!")
"""

# Vytvoření hlavního okna aplikace:
root = tk.Tk()

# Vytvoření názvu okna:
root.title("GUI Python")

# Nastavení šířky a výšky okna:
width = 500
height = 400
root.geometry(f"{width}x{height}")

# Vytvoření sítě:
cell_00 = tk.Label(root, text="       ."); cell_00.grid(row=0, column=0, sticky="w")
cell_01 = tk.Label(root, text="       ."); cell_01.grid(row=0, column=1, sticky="w")
cell_02 = tk.Label(root, text="       ."); cell_02.grid(row=0, column=2, sticky="w")
cell_03 = tk.Label(root, text="       ."); cell_03.grid(row=0, column=3, sticky="w")
cell_04 = tk.Label(root, text="       ."); cell_04.grid(row=0, column=4, sticky="w")
cell_05 = tk.Label(root, text="       ."); cell_05.grid(row=0, column=5, sticky="w")
cell_06 = tk.Label(root, text="       ."); cell_06.grid(row=0, column=6, sticky="w")
cell_07 = tk.Label(root, text="       ."); cell_07.grid(row=0, column=7, sticky="w")
cell_08 = tk.Label(root, text="       ."); cell_08.grid(row=0, column=8, sticky="w")
cell_09 = tk.Label(root, text="       ."); cell_09.grid(row=0, column=9, sticky="w")
cell_10 = tk.Label(root, text="       ."); cell_10.grid(row=0, column=10, sticky="w")
cell_11 = tk.Label(root, text="       ."); cell_11.grid(row=0, column=11, sticky="w")
cell_12 = tk.Label(root, text="       ."); cell_12.grid(row=0, column=12, sticky="w")
cell_13 = tk.Label(root, text="       ."); cell_13.grid(row=0, column=13, sticky="w")

# Vytvoření vlastního titulku:
title_label = tk.Label(root, text="Primitivní kalkulačka", font=("Helvetica", 14, "bold")); title_label.grid(row=1, column=1, columnspan=13, sticky="w")

# Prázdný řádek 1
empty_row1 = tk.Label(root, text="", width=10); empty_row1.grid(row=2, column=1, columnspan=13)

# Vytvoření instance písma
title_font = font.Font(family="Helvetica", size=14, weight="normal")
root.option_add("*Font", title_font)

# Vytvoření vstupních polí pro zadání čísel
label_num1 = tk.Label(root, text="Číslo 1:"); label_num1.grid(row=3, column=1, columnspan=4, sticky="w")
entry_num1 = tk.Entry(root); entry_num1.grid(row=3, column=4, columnspan=8, sticky="w")

label_num2 = tk.Label(root, text="Číslo 2:"); label_num2.grid(row=4, column=1, columnspan=4, sticky="w")
entry_num2 = tk.Entry(root); entry_num2.grid(row=4, column=4, columnspan=8, sticky="w")

# Prázdný řádek 2
empty_row2 = tk.Label(root, text="", width=10); empty_row2.grid(row=5, column=1, columnspan=13)

# Vytvoření rozbalovacího seznamu pro výběr operace
label_operation = tk.Label(root, text="Operace:"); label_operation.grid(row=6, column=1, columnspan=2, sticky="w")
combo_operation = tk.StringVar(); combo_operation.set("+")  # Výchozí hodnota
option_menu = tk.OptionMenu(root, combo_operation, "+", "-", "*", "/"); option_menu.grid(row=6, column=4, columnspan=8, sticky="w")

# Prázdný řádek 3
empty_row3 = tk.Label(root, text="", width=10); empty_row3.grid(row=7, column=1, columnspan=13)

# Vytvoření tlačítka pro provedení výpočtu
button_calculate = tk.Button(root, text="Spočítat", command=calculate); button_calculate.grid(row=8, column=4, columnspan=8, sticky="w")

# Prázdný řádek 4
empty_row4 = tk.Label(root, text="", width=10); empty_row4.grid(row=9, column=1, columnspan=13)

# Pole pro zobrazení výsledku
entry_result = tk.Entry(root); entry_result.grid(row=10, column=4, columnspan=8, sticky="w")

root.mainloop()

"""
# Použití kontejneru Pack

import tkinter as tk
from tkinter import messagebox
from tkinter import font

# Funkce pro provedení operace se zadanými čísly
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = combo_operation.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Chyba", "Nelze dělit nulou!")
                return

        messagebox.showinfo("Výsledek", f"Výsledek: {result}")

    except ValueError:
        messagebox.showerror("Chyba", "Zadávejte pouze čísla!")


root = tk.Tk()
root.title("GUI Python")

# Vytvoření vlastního titulku
title_label = tk.Label(root, text="Primitivní kalkulačka", font=("Helvetica", 18, "bold"))
title_label.pack(side="top", fill="x")

# Vytvoření instance písma
title_font = font.Font(family="Helvetica", size=12, weight="normal")
root.option_add("*Font", title_font)

# Nastavení šířky a výšky okna
width = 500
height = 500
root.geometry(f"{width}x{height}")

# Vytvoření vstupních polí pro zadání čísel
label_num1 = tk.Label(root, text="Číslo 1:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Číslo 2:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Vytvoření rozbalovacího seznamu pro výběr operace
label_operation = tk.Label(root, text="Operace:")
label_operation.pack()
combo_operation = tk.StringVar()
combo_operation.set("+")  # Výchozí hodnota
option_menu = tk.OptionMenu(root, combo_operation, "+", "-", "*", "/")
option_menu.pack()

# Vytvoření tlačítka pro provedení výpočtu
button_calculate = tk.Button(root, text="Spočítat", command=calculate)
button_calculate.pack()

root.mainloop()
"""
