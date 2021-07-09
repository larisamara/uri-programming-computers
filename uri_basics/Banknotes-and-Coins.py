n = float(input())
notas = int(n)
moedas = int((n-notas)*100)
n100 = notas//100
notas = notas%100
n50 = notas//50
notas = notas%50
n20 = notas//20
notas = notas%20
n10 = notas//10
notas = notas%10
n5 = notas//5
notas = notas%5
n2 = notas//2
notas = notas%2
m1 = notas//1
moedas = moedas%100
m50 = moedas//50
moedas = moedas%50
m25 = moedas//25
moedas = moedas%25
m10 = moedas//10
moedas = moedas%10
m05 = moedas//5
moedas = moedas%5
m01 = moedas//1
print("NOTAS:")
print("{:d} nota(s) de R$ 100.00".format(int(n100)))
print("{:d} nota(s) de R$ 50.00".format(int(n50)))
print("{:d} nota(s) de R$ 20.00".format(int(n20)))
print("{:d} nota(s) de R$ 10.00".format(int(n10)))
print("{:d} nota(s) de R$ 5.00".format(int(n5)))
print("{:d} nota(s) de R$ 2.00".format(int(n2)))
print("MOEDAS:")
print("{:d} moeda(s) de R$ 1.00".format(int(m1)))
print("{:d} moeda(s) de R$ 0.50".format(int(m50)))
print("{:d} moeda(s) de R$ 0.25".format(int(m25)))
print("{:d} moeda(s) de R$ 0.10".format(int(m10)))
print("{:d} moeda(s) de R$ 0.05".format(int(m05)))
print("{:d} moeda(s) de R$ 0.01".format(int(m01)))