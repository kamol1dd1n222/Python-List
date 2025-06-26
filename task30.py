sozlar = []
for i in range(5):
    soz = input(f"{i + 1} - so'zni kiriting: ")
    soz.lower()
    sozlar.append(soz)
palindromlar = []
for soz in sozlar:
    if soz == soz[::-1]:
        palindromlar.append(soz)

print(sozlar)
print(palindromlar)
