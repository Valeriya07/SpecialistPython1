# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

n = int(input ("Количество элементов"))
a=0
my_list=[]

import random
numbers = []
i=1
while i<=n:
    my_list.append(random.randint(-10, 10))
    i+=1
print(my_list)

for el in my_list:
    a=a+el
print (a)
