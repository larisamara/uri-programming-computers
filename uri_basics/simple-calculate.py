product_code, number_unity, value_unity = input().split()
value = int(number_unity) * float(value_unity)
product_code2, number_unity2, value_unity2= input().split()
value2 = int(number_unity2) * float(value_unity2)
print ("VALOR A PAGAR: R$", "%.2f" % (value + value2 ))