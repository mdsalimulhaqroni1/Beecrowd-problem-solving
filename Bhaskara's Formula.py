A,B,C = list(map(float, input().split()))
delta = B ** 2 - 4 * A * C

if delta < 0 or A == 0:
    print("Impossivel calcular")
else:
    X1 = (-B + (delta**(1/2)))/(2*A)
    X2 = (-B - (delta**(1/2)))/(2*A)

    print("X1 = %.5f"%X1)
    print("X2 = %.5f"%X2)
