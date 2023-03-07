a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
p=float((a+b+c)/2)
import math
S=round(math.sqrt(p*(p-a)*(p-b)*(p-c)),3)
if (a+b)>c and (a+c)>b and (b+c)>a:
    print("Dien tich=", S, sep='')
else:
    print("Khong hop le")