"15 вариант"
from random import randint
M = int(input("Введите количество строк:"))
N = int(input("Введите количество колонок:"))
c = int(input("Введите переменную c:"))
d = int(input("Введите переменную d:"))
R=[]

for i in range(M):
	b = []
	for j in range(N):
		b.append(randint(0,10))
	R.append(b)


for i in range(M):
	for j in range(N):
		print(R[i][j], end = ' ')
	print() 
for i in range(M):
	for j in range(N):
		if R[i][j]==c:
		   print("Строка №", i, "имеет такой элемент на", j+1, "месте")
		   s = []
		   for k in R[i]:
			   s.append(k*d)
		   print("Перемножим элементы на d и получим:",s)
		   print("===================================")

			
