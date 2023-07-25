a,b,c = map(float, input().split())

if a+b > c and a+c > b and b+c > a:
     print("Perimetro = %0.1f"%(a + b + c))
else:
    print("Area = %0.1f"%((c * (a + b)) / 2))