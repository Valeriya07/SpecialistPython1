# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

i=0
a=0
while i<len(my_list):
    if int(my_list[i])>0 and int(my_list[i])%2==0:
        a=a+int(my_list[i])
    i+=1
print(a)
