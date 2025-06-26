raqamlar = [3, 5, 2, 5, 1, 5, 2, 3, 2, 2]
counts = list()
for i in range(len(raqamlar)):
    cnt = raqamlar.count(raqamlar[i])
    counts.append(cnt) #raqamlar takrorlanganini sanab listga joylashtirdim
max_count = None
for i in range(len(counts)):
    max_count = counts[0]
    if counts[i] > max_count:
        max_count = counts[i] #eng ko'p tarqalgan birinchisini topdim
#   Ko'p tarqalganlarining eng birinchisini chiqarish
for i in range(len(raqamlar)):
    cnt = raqamlar.count(raqamlar[i])
    if cnt == max_count:
        print(raqamlar[i])
        break