def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount == 0:
            break
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

amount = 113
print(find_coins_greedy(amount))


def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_used = [0] * (amount + 1)
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin
    
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin
    
    return result


amount = 113
print(find_min_coins(amount)) 
