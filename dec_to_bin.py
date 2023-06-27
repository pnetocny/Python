bin_cislo = ("")
dec_cislo = input("Zadej celé kladné číslo (bez znaménka ´+´ pro převedení do binární soustavy: ")
if dec_cislo.isdigit() and int (dec_cislo) > 0:
    dec_cislo = int(dec_cislo) 
    while dec_cislo > 0:
        bin_pom = dec_cislo % 2 
        bin_cislo = str (bin_pom) + bin_cislo
        dec_cislo = dec_cislo // 2
    print ("Číslo převedené do binární soustavy je: ", bin_cislo)
else: 
    print ("Neplatný vstup. Zadej prosím celé kladné číslo.")
