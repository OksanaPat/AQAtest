import math
print("Введіть коефіцієнти для рівняння")
print("ax^2+bx+c=0:")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
discr = b**2-4*a*c
print(f"Дискримінант={discr}")
if discr >0:
    x1=(-b+math.sqrt(discr))/(2*a)
    x2=(-b-math.sqrt(discr))/(2*a)
    print(f"x1={x1}",f"x2={x2}")
if discr ==0:
    x=-b/(2*a)
    print(f"x={x}")
else:
    print("Коренів немає взагалі")