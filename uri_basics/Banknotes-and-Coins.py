n = float(input())
n100 = n//100
rest100 = n%100
n50 = rest100//50
rest50 = rest100%50
n20 = rest50//20
rest20 = rest50%20
n10 = rest20//10
rest10 = rest20%10
n5 = rest10//5
rest5 = rest10%5
n2 = rest5//2
rest2 = rest5%2
m1 = rest2//1
rest1 = rest2%1
m50 = rest1//0.50
rest050 = rest1%0.50
m25 = rest050//0.25
rest25 = rest050%0.25
m10 = rest25//0.10
rest010 = rest25%0.10
m05 = rest010//0.05
rest05 = rest010%0.05
m01 = rest05//0.01
print(n)
print("NOTAS:")
print("{:d} nota(s) de R$ 100.00".format(int(n100)))
print("{:d} nota(s) de R$ 50.00".format(int(n50)))
print("{:d} nota(s) de R$ 20.00".format(int(n20)))
print("{:d} nota(s) de R$ 10.00".format(int(n10)))
print("{:d} nota(s) de R$ 5.00".format(int(n5)))
print("{:d} nota(s) de R$ 2.00".format(int(n2)))
print("MOEDAS:")
print("{:d} moedas(s) de R$ 1.00".format(int(m1)))
print("{:d} moedas(s) de R$ 0.50".format(int(m50)))
print("{:d} moedas(s) de R$ 0.25".format(int(m25)))
print("{:d} moedas(s) de R$ 0.10".format(int(m10)))
print("{:d} moedas(s) de R$ 0.05".format(int(m05)))
print("{:d} moedas(s) de R$ 0.01".format(int(m01)))