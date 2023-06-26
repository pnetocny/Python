cely_cas_v_sekundach = int(input("Zadej počet sekund: "))
sekundy = cely_cas_v_sekundach % 60
sekundy = int(sekundy)
cely_cas_v_minutach = (cely_cas_v_sekundach - sekundy) / 60 
minuty = cely_cas_v_minutach % 60
minuty = int(minuty)
cely_cas_v_hodinach = (cely_cas_v_minutach - minuty) / 60
hodiny = cely_cas_v_hodinach % 60
hodiny = int(hodiny)
formatted_sekundy = "{:02}".format(sekundy)
formatted_minuty = "{:02}".format(minuty)
formatted_hodiny = "{:02}".format(hodiny)
print("sekundy: ", sekundy)
print("minuty: ", minuty)
print("hodiny: ", hodiny)
print((formatted_hodiny),  ":", (formatted_minuty), ":", formatted_sekundy)
