a, b = input().split()
if(int(b) <= 2 and int(b) >= 0):
    print("nova")
elif(int(b) <= 100 and int(b) >= 97):
    print("cheia")
elif(int(b) > int(a)):
    print("crescente")
else:
    print("minguante")