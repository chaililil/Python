"15 Задание"
from random import *
n = int(input("Введите длинну массива:"))
arr = [randint(0, 10) for i in range(n)]
print(arr)

zxc = []
for chislo in arr:
	if chislo % 2 != 0:
		zxc.append(chislo)
		
if len(zxc) == 0:
	print("Таких чисел нет")
	
zxc.reverse()
print("Нечетные числа:",zxc)
