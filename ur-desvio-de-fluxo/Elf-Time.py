n = input()
a, b = input().split()
result = 0
if(int(a) + int(b) <= int(n)):
   result = ("Farei hoje!")
if(int(a) + int(b) > int(n) ):
   result = ("Deixa para amanha!")
print(result)