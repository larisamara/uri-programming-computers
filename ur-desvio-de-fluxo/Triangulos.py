a, b, c = input().split()
if (((int(a) + int(b)) <= int(c)) and ((int(a) + int(c)) <= int(b)) and (int(b) + int(c)) <= int(a)):
    print("n")
elif (int(a) * 2) + (int(b) * 2) == int(c):
    print("a")

else:
    print("o")