a, b, c, d = input().split()
if int(a) + int(b) > int(c) and int(b) + int(c) > int(a) and int(a) + int(c) > int(b):
    print("S")
elif int(b) + int(c) > int(d) and int(c) + int(d) > int(b) and int(b) + int(d) > int(c):
    print("S")
elif int(a) + int(c) > int(d) and int(c) + int(d) > int(a) and int(a) + int(d) > int(c):
    print("S")
elif int(a) + int(b) > int(d) and int(b) + int(d) > int(a) and int(a) + int(d) > int(b):
    print("S")
else:
    print("N")