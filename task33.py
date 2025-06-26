list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
takrorlanganlar = list()
for i in list1:
    if i in list2 and i not in takrorlanganlar:
        takrorlanganlar.append(i)

print(takrorlanganlar)