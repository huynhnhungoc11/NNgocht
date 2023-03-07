a=int(input("Tieu Thu="))
dg1=550
dg2=750
dg3=950
dg4=1350

if a<=100:
    TienDien=a*dg1
elif a<=150:
    TienDien=100*dg1 + (a-100)*dg2
elif a<=200:
    TienDien=100*dg1 + 50*dg2 + (a-150)*dg3
else:
    TienDien=100*dg1 + 50*dg2 +50*dg3 + (a-200)*dg4
PhaiTra = TienDien*1.1
print("Phai tra=",PhaiTra,sep='')    