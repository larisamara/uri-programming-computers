start, end = input().split()
result = 0
if(int(start) < int(end)):
    result = int(end) - int(start)
    print("O JOGO DUROU", result, "HORA(S)") 
else:
    result = int(end) + 24 - int(start)
    print("O JOGO DUROU", result, "HORA(S)")
