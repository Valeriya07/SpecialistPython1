# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    a=int(str(ticket_number)[:1])+int(str(ticket_number)[1:2])+int(str(ticket_number)[2:3])
    b=int(str(ticket_number)[3:4])+int(str(ticket_number)[4:5])+int(str(ticket_number)[5:6])
    if a==b:
        print ('lucky')
    else:
        print ('not lucky')
    pass


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
