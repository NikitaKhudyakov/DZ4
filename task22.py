n = int(input("Размер первого: "))
m = int(input("Размер второго: "))
index = 0
list_1 = []
list_2 = []

for i in range(n):
    array = int(input("Введите числа для первого массива: "))
    list_1.append(array)
print(list_1)

for i in range(m):
    array = int(input("Введите числа для втрого массива: "))
    list_2.append(array)
print(list_2)

ar_1 = sorted(list_1)
ar_2 = sorted(list_2)

for i in ar_1:
    for j in ar_2:
        if i == j:
            print(f"Повтор числа - {i}")
    
