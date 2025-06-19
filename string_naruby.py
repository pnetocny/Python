print()
retezec_naruby = ""

retezec = input("Zadej libovolný řetězec: ")
delka_retezce = len(retezec)

for i in range(delka_retezce, 0, -1):
    retezec_naruby = retezec_naruby + retezec[i-1] 

print(retezec_naruby)
print()
