a, b, c, d = input().split()
x = int(a) * int(b)
y = int(c) * int(d)
result = 0
if x == y:
 result = 0
elif x > y:
 result = -1
else:
    result = 1
print(result)