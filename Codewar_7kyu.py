# 7 kyu


# Sum of the first nth term of Series

# def series_sum(n):
#     result = 1
#     if 0 <= n <= 1:
#         return str(n) + ".00"
#     else:
#         for i in range(1, n):
#             s = 1 / (1 + (3*i))
#             result += s
#         return "{:.2f}".format(result)


# print(series_sum(32))

# Get the Middle Character

# def get_middle(s):
#     l = int(len(s) / 2)
#     if len(s) % 2 == 0:
#         return s[l-1:l+1]
#     else:
#         return s[l]


# print(get_middle("testtest"))

# Maximum Length Difference

# s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
# s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]

# def mxdiflg(a1, a2):
#     result = []
#     if a1 != [] and a2 != []:
#         for x in a1:
#             for y in a2:
#                 z = abs(len(x)-len(y))
#                 result.append(z)
#         return max(result)
#     else:
#         return -1

# print(mxdiflg(s1,s2))