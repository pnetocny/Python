print()

# nastavení výchozí hodnoty (prázdný řetězec) pro binární číslo
bin_cislo = ("") 

# vložení čísla z klávesnice
dec_cislo = input("Zadej celé kladné číslo pro převedení do binární soustavy: ")

# rozdělení řetězce na první znak a ostatní znaky (pro následnou kontrolu)
prvni_znak = dec_cislo[0]
ostatni_znaky = "0" + dec_cislo[1:] 

if (prvni_znak == "+" or prvni_znak.isdigit()) and ostatni_znaky.isdigit():
    
    dec_cislo = int(dec_cislo) 
    while dec_cislo > 0:
        bin_pom = dec_cislo % 2 
        bin_cislo = str (bin_pom) + bin_cislo
        dec_cislo = dec_cislo // 2
    print ("Číslo převedené do binární soustavy je: ", bin_cislo)
else: 
    print ("Neplatný vstup. Zadej prosím celé kladné číslo.")
print()
