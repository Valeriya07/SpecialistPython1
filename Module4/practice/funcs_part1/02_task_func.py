# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def palindrome(number):
    r_number = number
    result = 0

    while (number != 0):
        digit = number % 10
        result = result * 10 + digit
        number = int(number / 10)

    if (result == r_number):
        return ("Palindrome!")
    return ("Not a Palindrome!")


# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
