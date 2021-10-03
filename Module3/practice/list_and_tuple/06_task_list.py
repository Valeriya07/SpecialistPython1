# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

my_list=list(range(first_number, second_number+1))
my_list_new=[]
for number in my_list:
    if number%3==0:
        my_list_new.append(number)
print(my_list_new)
