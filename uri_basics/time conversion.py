number = int(input())
m, s = divmod(number, 60)
h, m = divmod(m, 60)
print('{:d}:{:d}:{:d}'.format(h, m, s))