# Fabergé Easter Eggs crush test
def height(n, m):
    if n == 0 or m == 0:
        return 0

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1] + 1

    return dp[n][m]


print(height(0, 14))
print(height(2, 0))
print(height(2, 14))
print(height(7, 20))
# print(height(7, 500))
# print(height(9477, 10000))
