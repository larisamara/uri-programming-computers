product_code = input()
number_unity = input()
value_unity = input()
value = int(number_unity) * float(value_unity.replace(',','.'))
product_code2 = input()
number_unity2 = input()
value_unity2 = input()
value2 = int(number_unity2) * float(value_unity2.replace(',','.'))
print ("VALOR A PAGAR: R$ ", "%.2f" % (value + value2 ))