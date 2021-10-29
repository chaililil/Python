"15 Задание"
from random import *
n = int(input("Введите длинну массива:"))
arr = [randint(0, 10) for i in range(n)]
print(arr)

zxc = []
for qwe in set(arr):
    if arr.count(qwe)>1:
        zxc.append(qwe)
print("Повторяющиеся значения:",zxc)
