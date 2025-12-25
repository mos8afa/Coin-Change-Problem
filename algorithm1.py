def coin_change_naive(coins, amount):

    def solve(rem):
        if rem == 0:
            return 0             
        if rem < 0:
            return float('inf')   
        
        best = float('inf')
        for c in coins:
            res = solve(rem - c)  
            if res != float('inf'):
                best = min(best, res + 1)

        return best

    ans = solve(amount)
    return -1 if ans == float('inf') else ans


# مثال
coins = [1,2]   
amount = 4
print(coin_change_naive(coins, amount))  # 2