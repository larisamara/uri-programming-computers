qtd = int(input())
min_lavadora, max_lavadora = input().split()
min_secadora, max_secadora = input().split()
if (qtd >= int(min_lavadora) and qtd <= int(max_lavadora)) and (qtd >= int(min_secadora) and qtd <= int(max_secadora)):
     print("possível")
else:
     print("impossível")