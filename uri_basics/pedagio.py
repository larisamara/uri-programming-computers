length, distance = input().split()
cost_kilometer, cost_toll = input().split()
spent_kilometer_total = int(cost_kilometer) * int(length)
qtd_toll = int(length) / int(distance)
spent_toll = int(qtd_toll) * int(cost_toll)
result = spent_kilometer_total + spent_toll
print(result) 