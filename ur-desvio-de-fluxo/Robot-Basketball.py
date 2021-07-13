d = input()
result = 0
if(int(d) <= 800):
    result = 1
if(int(d) > 800 and int(d) <= 1400):
    result = 2
if(int(d) > 1400 and int(d)<= 2000):
    result = 3
print(result)
