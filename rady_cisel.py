cislo1 = 0
cislo2 = 1
cislopom = cislo1 + cislo2 
i = int(input("Zadej počet opakování pro Fibonacciho posloupnost: "))
for i in range (1, i + 1):
    cislopom = cislo1 + cislo2
    print(cislo1, " + ", cislo2, " = " , cislopom)
    cislo1 = cislo2 
    cislo2 = cislopom
print("Poměr mezi číslem 2 a číslem 1 je : ", round(cislo2 / cislo1, 10))
