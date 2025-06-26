sonlar = [1, 2, 3, 7, 8, 9]

onlik_list = list()
for i in range(len(sonlar)):
    for j in range(i + 1,len(sonlar)):
        
        if (sonlar[i] + sonlar[j]) == 10:
            onliklar = [sonlar[i] , sonlar[j]]
            j = len(sonlar) - 1
    if onliklar not in onlik_list:
        onlik_list.append(onliklar)        
print(onlik_list)