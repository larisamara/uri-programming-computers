a, b, c = input().split()
value1 = int(a) 
value2 = int(b)
value3 = int(c)
if value1 > value2:
    aux = value2
    value2 = value1
    value1 = aux
if value2 > value3:
    aux = value3
    value3 = value2
    value2 = aux
if value1 > value2:
    aux = value2
    value2 = value1
    value1 = aux
print(value1)
print(value2)
print(value3)
print()
print(a)
print(b)
print(c)

