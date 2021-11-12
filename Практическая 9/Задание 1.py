"15 вариант"
n = int(input("Введите размер матрицы:"))
c = int(input("Введите переменную c:"))
d = int(input("Введите переменную d:"))
R=[]

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
	for j in range(n):
		if R1[i][j]==c:
		   print("Строка №", i, "имеет такой элемент на", j+1, "месте")
		   s = []
		   for k in R1[i]:
			   s.append(k*d)
		   print("Перемножим элементы на d и получим:",s)
		   print("===================================")	
		   file1.write("Результат ")
		   file1.write(str(i+1))
		   file1.write(": ")
		   file1.write(str(s))
		   file1.write("\n")
file1.close()
