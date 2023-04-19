n = int(input("Введите число кустов: "))
list_1 = []
for i in range(n):
    array = int(input("Введите количество ягод на кусте: "))
    list_1.append(array)
print(list_1)
i = 0 
max = 0
for i in range(len(list_1)):
    sum = (list_1[i-2]) + (list_1[i-1]) + (list_1[i])
    if max < sum:
        max = sum
print(f"Mаксимальное количество ягод которое можно собрать - {max}!")
  