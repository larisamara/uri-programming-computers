a = int(input())
b = int(input())
c = int(input())
andar1 = (b + c) * 2
andar2 = (a + c) * 2
andar3 = (a + b) * 2
if andar1 < andar2:
    print(int(andar1))
elif andar2 < andar1:
    print(int(andar2))
else: 
    print(int(andar3))