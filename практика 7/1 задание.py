"15 вариант."

n = int(input("Введите число n:"))

def numbers(s):
    
    if (bin(s)[2:] == bin(s)[2:][::-1]):
        return s
    else:
        return ""

for s in range(2,n+1):
    qwe = 1
    for i in range(2,s):
        if (s%i==0):
            qwe = 0
    if qwe:
        print (numbers(s))
