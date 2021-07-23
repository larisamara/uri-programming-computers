alcool, gasolina, preco_alcool, preco_gasolina = input().split()
if (float(preco_alcool) / float(alcool)) <= (float(preco_gasolina) / float(gasolina)):
    print("G")
else:
    print("A")