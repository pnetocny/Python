bin_cislo = ("")
bin_pom = 0
dec_cislo = int(input("Zadej celé kladné číslo pro převedení do binární soustavy: "))
while dec_cislo > 0:
    bin_pom = dec_cislo % 2 
    bin_cislo = str (bin_pom) + bin_cislo
    dec_cislo = dec_cislo // 2
print ("Číslo převedené do binární soustavy je: ", bin_cislo)
