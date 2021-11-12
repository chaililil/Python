"15 вариант"
from random import randint
n = int(input("Введите размер матрицы:"))

R=[]
t = int(0)
sum = int(0)
max = int(0)

file = open("Якубов Я.А._Уб-11_vvod.txt", "r")

for i in range(n):
	b = []
	for j in range(n):
		b.append(file.read(1))
	R.append(b)
file.close()

R1 = []
for i in range(n):
    l = []
    for j in range(n):
        l.append(int(R[i][j]))
    R1.append(l)

for i in range(n):
    for j in range(n):
        print(R1[i][j], end= " ")
    print()	

file1 = open("Якубов Я.А._Уб-11_vivod.txt","w") 
for i in range(n):
	
		item_list = R1[i]
		p = all(item%2!=0 for item in item_list)
		if p == True:
			print("Содержат только нечетные элементы строки -", i)
			file1.write("Результат ")
			file1.write(str(i+1))
			file1.write(": ")
			file1.write(str(i))
			file1.write("\n")
file1.close()

"Я не понял как суммировать элементы"


		
			
		   

			
