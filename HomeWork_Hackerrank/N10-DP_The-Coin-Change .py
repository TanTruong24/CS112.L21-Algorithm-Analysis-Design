def getNumberOfWays(N, m, Coins):

    ways = [0] * (N + 1)

    # Set the first way to 1 because its 0 and
    # there is 1 way to make 0 with 0 coins
    ways[0] = 1

    for i in range(m):

        for j in range(N+1):
            if (Coins[i] <= j):

                # Update the ways array
                ways[j] += ways[(int)(j - Coins[i])]

    # return the value at the Nth position
    return ways[N]

n, m = map(int, input().split())
coins = list(map(int, input().split()))
print(getNumberOfWays(n, m, coins))


