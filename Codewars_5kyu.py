# # # Sum of Pairs
# l1 = [1, 4, 8, 7, 3, 15]
# l2 = [1, -2, 3, 0, -6, 1]
# l4 = [1, 2, 3, 4, 1, 0]
# s = 8
# s1 = -6
# s2 = 2
# def sum_pairs(ints, s):
#     myset = set()
#     for num in ints:
#         required = s - num
#         if required in myset:
#             return [required, num]
#         myset.add(num)
# print(sum_pairs(l4,s2))
                



# Directions Reduction
# a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# def dirReduc(arr):
#     dict = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
#     res = []
#     for i in arr:
#         if res and dict[i] == res[-1]:
#             res.pop()
#         else:
#             res.append(i)
#     return res
# print(dirReduc(a))



#  String incrementer
# a = "foobar23"
# def increment_string(strng):
#     result = strng.rstrip("0123456789")
#     l = strng[len(result):]
#     if l == "": 
#         return strng+"1"
#     else:
#         return result + str(int(l) + 1).zfill(len(l))
# print(increment_string(a))



# Regex Password Validation
# regex = r'^(?=[0-9a-zA-Z]{6,}$)(?=[0-9a-zA-Z]*[A-Z])(?=[0-9a-zA-Z]*[a-z])(?=[0-9a-zA-Z]*[0-9]).*'
# # 大佬鼠
# regex0 = (
#     '^'            # start line
#     '(?=.*\d)'     # must contain one digit from 0-9
#     '(?=.*[a-z])'  # must contain one lowercase characters
#     '(?=.*[A-Z])'  # must contain one uppercase characters
#     '[a-zA-Z\d]'   # permitted characters (alphanumeric only)
#     '{6,}'         # length at least 6 chars
#     '$'            # end line
# )
# regex1="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"



# Maximum subarray sum
# def max_sequence(arr):
#     max = 0
#     max_1 = 0
#     for i in arr:
#         if max_1 > 0:
#             max_1 += i
#             if max_1 < 0:
#                 max_1 = 0
#             elif max_1 > max:
#                 max = max_1
#         elif i > 0:
#             max_1 += i
#     return max



# Rot13
# a = 'abcdefghijklmnopqrstuvwxyz'
# def rot13(message):
#     result = ''
#     for i in message:
#         if i.islower():
#             if ord(i)+13 >= 123:
#                 result += chr(ord(i)+13-26)
#             else:
#                 result += chr(ord(i)+13)
#         elif i.isupper():
#             j = i.lower()
#             if ord(j)+13 >= 123:
#                 result += chr(ord(j)+13-26).upper()
#             else:
#                 result += chr(ord(j)+13).upper()
#         else:
#             result += i
#     return result

# print(rot13(a))



# Gap in Primes
def gap(g, m, n):
    primes_number = []
    for num in range(m,n+1):
        number_of_dividers = 0
        for divider in range(1,num+1):
            if num % divider == 0:
                number_of_dividers += 1
            if number_of_dividers > 2:
                break
        if number_of_dividers == 2:
            primes_number.append(num)
    for i in range(0,len(primes_number)-1):
        if primes_number[i+1] - primes_number[i] == g:
            return [primes_number[i], primes_number[i+1]]
    return None

print(gap(8,300,400))
print(gap(6,100,110))
print(gap(10,300,400))