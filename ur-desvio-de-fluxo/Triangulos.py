a, b, c = input().split()
if int(a) ** 2 < (int(b) ** 2) + (int(c) ** 2):
    print("a")
elif int(a) ** 2 == (int(b) ** 2) + (int(c) ** 2):
    print("r")
elif int(a) ** 2 > (int(b) ** 2) + (int(c) ** 2):
    print("o")
else:
    print("n")
Triângulo acutângulo: A² < B² + C²
Triângulo retângulo: A² = B² + C²
Triângulo obtusângulo: A² > B² + C²