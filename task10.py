lst = [10,20,30,40,50,60,70,80,90]
print("\t\t\n\nBoshlang'ich list\n",lst)
new_index = int(input("Index: "))
new_qiymat = input("Yangi qiymat: ")
l = len(lst)
if -l <= new_index <= l - 1:
    lst.insert(new_index,new_qiymat)
else:
    print("\n\t\tNoto'g'ri index kiritildi!")
print("\t\t Yangilangan list \n",lst)