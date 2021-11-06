"15 вариант"
from random import randint
M = int(input("Введите количество строк:"))
N = int(input("Введите количество колонок:"))
R=[]
t = int(0)
sum = int(0)
max = int(0)

for i in range(M):
	b = []
	for j in range(N):
		b.append(randint(0,10))
	R.append(b)	    
	
for i in range(M):
	for j in range(N):
		"Для того, чтобы точно были нечетные"
		R[2][0] = 3
		R[2][1] = 5
		R[2][2] = 9

for i in range(M):
	for j in range(N):
		print(R[i][j], end = " ")
	print() 
for i in range(M):
	
		item_list = R[i]
		p = all(item%2!=0 for item in item_list)
		if p == True:
			print("Содержат только нечетные элементы строки -", i)
"Я не понял как суммировать элементы"


		
			
		   

			
