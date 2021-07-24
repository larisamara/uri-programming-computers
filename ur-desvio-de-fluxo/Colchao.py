a, b, c = input().split()
h, l = input().split()
if int(a) <= int(h) and int(b) <= int(l):
    print("S")
elif int(a) <= int(h) and int(c) <= int(l):
    print("S")
elif int(b) <= int(h) and int(a) <= int(l):
    print("S")
elif int(b) <= int(h) and int(c) <= int(l):
    print("S")
elif int(c) <= int(h) and int(a) <= int(l):
    print("S")
elif int(c) <= int(h) and int(b) <= int(l):
    print("S")
else:
    print("N")