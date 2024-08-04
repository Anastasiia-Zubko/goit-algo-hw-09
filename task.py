import time

def find_coins_greedy(amount):
    """
    Function to find the minimum coins using the greedy approach.
    """
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            result[coin] = count

    return result

def find_min_coins(amount):
    """
    Function to find the minimum coins using dynamic programming.
    """
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

def compare_algorithms(amount):
    """
    Function to compare the performance of greedy and dynamic programming algorithms.
    """
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time

    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time

    print(f"Greedy Result: {greedy_result}, Time: {greedy_time:.6f} seconds")
    print(f"Dynamic Programming Result: {dp_result}, Time: {dp_time:.6f} seconds")

def main():
    """
    Main function to run the comparison.
    """
    amount = 113
    compare_algorithms(amount)

if __name__ == "__main__":
    main()
