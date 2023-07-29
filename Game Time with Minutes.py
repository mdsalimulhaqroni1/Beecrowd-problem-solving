a,b,c,d = map(int, input().split())

start = a * 60 + b
end = c * 60 + d

duration = end - start
if duration <= 0:
    duration += 24 * 60
hours = duration // 60
minutes = duration % 60

print(f"O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)")
