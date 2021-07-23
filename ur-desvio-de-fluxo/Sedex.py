bola = int(input())
altura, largura, profundidade = input().split()
if int(altura) >= bola and int(largura) >= bola and int(profundidade) >= bola:
    print("S")
else:
    print("N")