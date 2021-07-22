start, end = input().split()
result = 0
if (int(start) < int(end)):
    result = int(start) - int(end)
    print("O JOGO DUROU",result,"HORA(S)") 
elif (int(start) > int(end)):
    result = (int(end) + 24) - int(start)
    print("O JOGO DUROU",result,"HORA(S)")
else:
    print("O JOGO DUROU 24 HORA(S)")