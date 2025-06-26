harfli3 = list()
harfli4_6 = list()
harfli6_plus = list()
ismlar = [
    "Azizbek", "Ziyoda", "Shahzoda", "Jasur", "Dilnoza",
    "Ulug'bek", "Ali", "Sherzod", "Lola", "Muhammadali"
]

print(ismlar)
for i in ismlar:
    if len(i) <= 3:
        harfli3.append(i)
    elif 4 <= len(i) <= 6:
        harfli4_6.append(i)
    else:
        harfli6_plus.append(i)
print("<=3:   \n\t\t",harfli3)     
print("4 <= harflar <=6:   \n\t\t",harfli4_6)  
print(">= 6:   \n\t\t",harfli6_plus)    