value = int(input())
years = value // 365
value = value % 365
months = value // 30
value = value % 30
days = value
print(years, "ano(s)")
print(months, "mes(es)")
print(days, "dia(s)")