"15 вариант"
"КОД РАБОТАЕТ НЕДО КОНЦА(Я НЕ ЗНАЮ КАК ВЫДЕЛИТЬ ТОЛЬКО МИНИМУМ)"
import math

def q(x1,x2,x3,t1,t2,t3):
     dist = math.sqrt((t1 - x1)**2 + (t2 - x2)**2 + (t3 - x3)**2)
     return dist
def qw(x1,x2,x3,z1,z2,z3):
     dist = math.sqrt((z1 - x1)**2 + (z2 - x2)**2 + (z3 - x3)**2)
     return dist
def qwe(x1,x2,x3,y1,y2,y3):
     dist = math.sqrt((y1 - x1)**2 + (y2 - x2)**2 + (y3 - x3)**2)
     return dist
def qwer(y1,y2,y3,t1,t2,t3):
     dist = math.sqrt((t1 - y1)**2 + (t2 - y2)**2 + (t3 - y3)**2)
     return dist
def qwert(y1,y2,y3,z1,z2,z3):
     dist = math.sqrt((z1 - y1)**2 + (z2 - y2)**2 + (z3 - y3)**2)
     return dist
def qwerty(z1,z2,z3,t1,t2,t3):
     dist = math.sqrt((t1 - z1)**2 + (t2 - z2)**2 + (t3 - z3)**2)
     return dist
x1 = int(input("Введите первую координату для точки X:"))
x2 = int(input("Введите вторую координату для точки X:"))
x3 = int(input("Введите третью координату для точки X:"))
y1 = int(input("Введите первую координату для точки Y:"))
y2 = int(input("Введите вторую координату для точки Y:"))
y3 = int(input("Введите третью координату для точки Y:"))
z1 = int(input("Введите первую координату для точки Z:"))
z2 = int(input("Введите вторую координату для точки Z:"))
z3 = int(input("Введите третью координату для точки Z:"))
t1 = int(input("Введите первую координату для точки T:"))
t2 = int(input("Введите вторую координату для точки T:"))
t3 = int(input("Введите третью координату для точки T:"))
print ("---------------------------------------------------")
print ("Расстояние между точками X и Y :",q(x1,x2,x3,y1,y2,y3))
print ("Расстояние между точками X и Z :",qw(x1,x2,x3,z1,z2,z3))
print ("Расстояние между точками X и T :",qwe(x1,x2,x3,t1,t2,t3))
print ("Расстояние между точками Y и T :",qwer(y1,y2,y3,t1,t2,t3))
print ("Расстояние между точками Y и Z :",qwert(y1,y2,y3,z1,z2,z3))
print ("Расстояние между точками Z и T :",qwerty(z1,z2,z3,t1,t2,t3))
