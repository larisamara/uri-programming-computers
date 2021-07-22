a, b, c = input().split()
if (int(a) - int(b) == 0):
    print("S")
elif (int(a) - int(c) == 0):
    print("S")
elif (int(b) - int(c) == 0):
    print("S")
elif ((int(a) +int(b)) - int(c) == 0):
    print("S")   
elif  ((int(a) +int(c)) - int(b) == 0):
    print("S") 
elif ((int(c) +int(b)) - int(a) == 0):
    print("S") 
else:
    print("N")