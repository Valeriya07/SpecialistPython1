# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# Найдите:
dupl=[]
for item in items:
    dupl.append(item['brand'])
woduplicates = set(dupl)
print("Товары на складе представлены брэндами: ",woduplicates)


print("На складе больше всего товаров брэнда(ов): ")
from collections import Counter

c = Counter(dupl)

print(c.most_common())


print("На складе самый дорогой товар брэнда(ов): ")

max_p=items[0]
for p in items:
    if p['price']>max_p['price']:
        max_p=p
print(max_p['brand'])
