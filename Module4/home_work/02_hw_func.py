# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(Xa, Ya, Xb, Yb,Xc, Yc):
    ab= ((abs(Xb - Xa))**2+(abs(Yb-Ya))**2)**0.5
    bc = ((abs(Xb - Xc)) ** 2 + (abs(Yb- Yc)) ** 2) ** 0.5
    ac = ((abs(Xa - Xc)) ** 2 + (abs(Ya - Yc)) ** 2) ** 0.5
    if ab<=bc and ab<=ac:
        print("Самый короткий отрезок ab")
    elif bc<=ab and bc<=ac:
        print("Самый короткий отрезок bc")
    else:
        print("Самый короткий отрезок ac")
    pass

print(distance(1, 1, 4, 2,3, 4))
