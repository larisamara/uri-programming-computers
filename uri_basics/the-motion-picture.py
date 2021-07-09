number1, number2 = input().split()
value =(float(number1) - float(number2))
percent = (abs(value) / float(number1)) * 100 
print(str("%.2f" % percent + "%"))