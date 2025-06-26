ismlar = [
    "Azizbek", "Ziyoda", "Shahzoda", "Jasur", "Dilnoza",
    "Ulug'bek", "Madina", "Sherzod", "Lola", "Muhammadali"
]

lens = list()
for i in ismlar:
    lens.append(len(i))

max_ism = 0 # Ism uzunligi 0 dan kichik emas shuning uchun 0 ga tengladim None qo'ysam ishlamadi
for i in lens:
    if i > max_ism:
        max_ism = i

for i in ismlar:
    if len(i) == max_ism:
        print(i)
        break