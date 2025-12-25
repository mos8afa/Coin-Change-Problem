"""
def coin_change_with_coins(coins, amount):
    INF = amount + 1

    dp = [INF] * (amount + 1)     
    pick = [-1] * (amount + 1)    

    dp[0] = 0

    for x in range(1, amount + 1):
        for c in coins:
            if x - c >= 0 and dp[x - c] + 1 < dp[x]:
                dp[x] = dp[x - c] + 1
                pick[x] = c

    if dp[amount] == INF:
        return -1, []  

    used = []
    cur = amount
    while cur > 0:
        c = pick[cur]
        used.append(c)
        cur -= c

    return dp[amount], used

coins = [1, 5, 10, 20, 50, 100, 200]
amount = 27
count, used_coins = coin_change_with_coins(coins, amount)
print("Amount:",amount)
print("Min coins:", count)
print("Coins used:", used_coins)

"""
def coin_change_optimized(coins, amount):
    IMP = amount + 1

    mc = [IMP] * (amount + 1)
    mc[0] = 0
                     
    for x in range(1, amount + 1): 
        for c in coins: 
            if x - c >= 0:          
                mc[x] = min(mc[x], mc[x - c] + 1)

    return -1 if mc[amount] == IMP else mc[amount] #mc[4]=2


# Example
coins = [1,2]
amount = 4
print(coin_change_optimized(coins, amount))  # Output: 2
