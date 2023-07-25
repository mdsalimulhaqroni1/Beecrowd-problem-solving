X,Y = map(int, input().split())
if X == 1:
    total = 4.00 * Y
elif X == 2:
    total = 4.50 * Y
elif X == 3:
    total = 5.00 * Y
elif X == 4:
    total = 2.00 * Y
elif X == 5:
    total = 1.50 * Y

print("Total: R$ %.2f"%total)