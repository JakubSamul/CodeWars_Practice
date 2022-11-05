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



# Simple Fun #176: Reverse Letter
# def reverse_letter(string):
#     result = ""
#     for text in string[::-1]:
#         if text.isalpha() == True:
#             result += text
#     return result
# print(reverse_letter("ultr53o?n"))



# # Check the exam
# a = ["a", "a", "b", "b"]
# b = ["a", "c", "b", "d"]
# def check_exam(arr1,arr2):
#     count = 0 
#     for i in range(0,len(arr1)):
#         if arr1[i] == arr2[i] and arr2[i] != "":
#             count += 4
#         elif arr1[i] != arr2[i] and arr2[i] != "":
#             count -= 1
#         else:
#             count += 0
#     if count < 0:
#         return 0
#     else:
#         return count
# print(check_exam(a,b))



# # Alternate capitalization
# a = "abcdef"
# b = "abracadabra"
# def capitalize(s):
#     for i in range(0,len(s),2):
#         s[i] = s[i].upper()
#         print(s)
# print(capitalize(a))



# a = [1,2,3,4,3,3,5,1,0]
# print(set(a))


class A:
    def __init__(self, val):
        self.val = val

    def __eq__(self, target):
        return self.val == target.val

    def __lt__(self, target):
        return self.val == target.val

    def __gt__(self, target):
        return self.val == target.val
 
 
from collections import Counter



a = 'asdasdasdasdas'

def zad(a):
    result = Counter(a)
    return result.most_common()[0]

print(zad(a))