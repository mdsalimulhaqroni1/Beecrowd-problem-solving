product1 = input().split(" ")
product2 = input().split(" ")
code1, units1, price1 = product1
code2, units2, price2 = product2
total = (int(units1) * float(price1)) + (int(units2) * float(price2))
print("VALOR A PAGAR: R$ %.2f" %total)
