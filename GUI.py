# GUI

#Importování knihovny:
import tkinter as tk

# Vytvoření hlavního okna aplikace:
window = tk.Tk()

# Vytvoření názvu okna:
window.title("GUI for Python")

# Nastavení šířky a výšky GUI okna:
width = 500
height = 500
window.geometry(f"{width}x{height}")

# Vytvoření vlastního titulku:
title_label = tk.Label(window, text=" Vítejte v mé aplikaci! :-) ", font=("Courier", 16, "bold")); title_label.grid(row=1, column=0, columnspan=2, sticky="ew")

# Spuštění hlavní smyčky aplikace:
window.mainloop()
