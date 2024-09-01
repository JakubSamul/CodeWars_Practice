# # Fabergé Easter Eggs crush test
# import time


# def height(n, m):
#     start_1 = time.time()
#     if n == 0 or m == 0:
#         return 0

#     dp = [[0] * (m + 1) for _ in range(n + 1)]
#     start_2 = time.time()
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1] + 1
#     start_3 = time.time()
#     print(dp)
#     # print(start_3 - start_2, start_2 - start_1)
#     return dp[n][m]


# # print(height(0, 14))
# # print(height(2, 0))
# print(height(4, 5))
# # print(height(7, 20))
# # print(height(9477, 1000))
# # print(height(9477, 10000))
