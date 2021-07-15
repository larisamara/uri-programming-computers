a = int(input())
b = int(input())
c = int(input())
andar1 = 2 * b + 4 * c
andar2 = 2 * a + 2 * c
andar3 = 2 * b + 4 * a
if andar1 <= andar2 and andar1 <= andar3:
    print(int(andar1))
elif andar2 <= andar1 and andar2 <= andar3:
    print(int(andar2))
else: 
    print(int(andar3))