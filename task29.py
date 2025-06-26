numbers = list() 
for i in range(10):
    son = int(input(f"{i + 1} - son: "))
    numbers.append(son)
print(numbers)
new_lst = list()
for i in range(len(numbers)):
    cnt=  numbers.count(numbers[i])
    if cnt == 1: 
        new_lst.append(numbers[i])
print(new_lst)