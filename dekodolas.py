import os
os.system('cls')


with open("morsekodok.txt", "r", encoding="utf-8") as file:
    kod_lista = []
    for sor in file:
        reszek = sor.strip().split()
        if len(reszek) == 2:
            betu, kod = reszek
            kod_lista.append((betu, kod))


bemenet = input("Írj be egy morse kódot ").strip()

morse_jelek = bemenet.split(" / ")

eredmeny = []

for kod in morse_jelek:
    if kod == "":
        continue  
  
    for betu, morse in kod_lista:
        if kod == morse:
            eredmeny.append(betu)
            break
    else:
        if kod == "":
            continue
        elif kod == "/":
            eredmeny.append(" ")  
        else:
            eredmeny.append("?")  


print(" A szöveg eredménye:", "".join(eredmeny))

