# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

sum_p=0

def gen_list(a, b):
    my_list = list(range(a, b + 1))
    return my_list


def palindrome(number):
    r_number = number
    result = 0

    while (number != 0):
        digit = number % 10
        result = result * 10 + digit
        number = int(number / 10)
    return result == r_number


for _ in gen_list(11, 55):
    if palindrome(_):
        sum_p+=1

print (sum_p)
