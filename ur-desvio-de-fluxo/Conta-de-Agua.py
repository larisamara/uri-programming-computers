consumo_agua = int(input())
consumo = 7
if  consumo_agua >= 11 and consumo_agua <= 30:
    consumo = ((consumo_agua - 10) * 1) + 7
elif consumo_agua >= 31 and consumo_agua <= 100:
    consumo = (consumo_agua - 30) * 2 + 27
elif consumo_agua >= 101:
    consumo = (consumo_agua - 100) * 5 + 167
print(consumo)