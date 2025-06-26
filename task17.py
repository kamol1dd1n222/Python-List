lst = list()
print("\t\t\tIsmlar soni tugasa tugadi deb kiriting!")
for i in range(1000000000000000):
    name = input("Ism:  ")
    if name.lower() != 'tugadi':
        lst.append(name)
    else:
        break
print(lst)
print(len(lst))