def gas_station(gas,cost):
    remaining = 0
    candidate = 0
    prev_remaining = 0
    for i in range(len(gas)):
        remaining += gas[i] - cost[i]
        if remaining<0:
            candidate = i+1
            prev_remaining += remaining
            remaining = 0
    if candidate == len(gas) or remaining+prev_remaining <0 :
        return -1
    else:
        return candidate
gas =  [2,2,2,2,2,2,2,2,2]
cost = [1,1,1,1,1,1,1,1,50]
print(gas_station(gas,cost))