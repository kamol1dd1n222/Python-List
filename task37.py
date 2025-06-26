list1 = [1, 2, 3] 
list2 = [4, 5, 6]
for i in range(len(list1)):
    list1.insert(i,list2[i])
    list2.insert(i,list1[i + 1])
    list1.pop(i + 1)
    list2.pop(i + 1)
print(list1)
print(list2)