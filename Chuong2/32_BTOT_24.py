print("Dien tich cua mot tam giac theo do dai cua cac canh ")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
S=float((a+b+c)/2)
d=float(S*(S-a)*(S-b)*(S-c))
import math
print("Dien tich=", math.sqrt(d), sep='')