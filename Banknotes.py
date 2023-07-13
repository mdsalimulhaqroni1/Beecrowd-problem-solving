
N = int(input())
print(N)

notes_100 = N // 100
N = N % 100
notes_50 = N // 50
N = N % 50
notes_20 = N // 20
N = N % 20
notes_10 = N // 10
N = N % 10
notes_5 = N // 5
N = N % 5
notes_2 = N // 2
N = N % 2
notes_1 = N

print(notes_100, "nota(s) de R$ 100,00")
print(notes_50, "nota(s) de R$ 50,00")
print(notes_20, "nota(s) de R$ 20,00")
print(notes_10, "nota(s) de R$ 10,00")
print(notes_5, "nota(s) de R$ 5,00")
print(notes_2, "nota(s) de R$ 2,00")
print(notes_1, "nota(s) de R$ 1,00")