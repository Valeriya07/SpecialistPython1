# Напишите функцию находящую n-ое число Фибоначчи.
def fib(n):
    fib1 = 1
    fib2 = 1

    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib2

print("Значение этого элемента:", fib(6))
