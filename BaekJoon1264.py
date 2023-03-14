import copy

egg_and_consumer = list(map(int, input().split()))
suggest_cost = []
profit = []

for i in range(egg_and_consumer[1]) :
    suggest_cost.append(int(input()))

suggest_cost.sort()
profit = copy.deepcopy(suggest_cost)

for i in range(egg_and_consumer[1], 0, -1) :
    if i> egg_and_consumer[0] :
        profit[egg_and_consumer[1]-i] *= egg_and_consumer[0]
    else:    
        profit[egg_and_consumer[1]-i] *= i

print(suggest_cost[profit.index(max(profit))], profit[profit.index(max(profit))])