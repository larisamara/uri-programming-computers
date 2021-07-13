line =  int(input())
column = int(input())
if (line%2!=0):
    if (column%2!=0):
        print("1")
    else:
        print("0")
elif (line%2==0):
    if (column%2==0):
        print("1")
    else:
        print("0")