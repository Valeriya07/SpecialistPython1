# Напишите программу, которая запрашивает строку до тех пор, пока пользователь не введет “хватит”.
# Т.е. программа запрашивает ввод, если вводится любое значение отличное от слова “хватит”,
# то программа запрашивает ввод снова.

word = str(input("Слово: "))
while word!="хватит":
    print ("Попробуй еще раз")
    word = str(input("Слово: "))
