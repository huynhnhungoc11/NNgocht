kq = 0
a = float(input('x='))
b = float(input('y='))
S = str(input('Phep toan: '))

if S == "+":
    kq =a+b
    print(a,'+',b,'=',kq,sep='')
elif S == "-":
    kq =a-b    
    print(a,'-',b,'=',kq,sep='')
elif S == "*":    
    kq =a*b
    print(a,'*',b,'=',kq,sep='')
elif S == "/":
   if (b != 0):
    kq =a/b
    print(a,'/',b,'=',kq,sep='')
   else:
    print('Khong hop le')
else:
    print("Khong hop le")