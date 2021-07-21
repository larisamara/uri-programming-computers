number1, number2 = input().split()
if int(number1) > int(number2):
 if int(number1) % int(number2) == 0:
     print("Sao Multiplos")
 else: 
    print("Nao sao Multiplos")
if int(number1) == int(number2):
    print("Sao Multiplos")
if int(number2) > int(number1):
 if int(number2) % int(number1) == 0:
     print("Sao Multiplos")
 else: 
    print("Nao sao Multiplos")