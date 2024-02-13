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
def prime(i):
    if i <=0 or i == 1:
        return False
    j = 2
    while(j <= i ** 0.5):
        if i % j ==0:
            return False
        j += 1
    return True

def gap(g, m, n):
    number = 0
    result = 0
    for i in range(m,n+1):
        if prime(i):
            if number == 0:
                number = i
            elif result == 0:
                result = i
            else:
                number = result
                result = i
        if result - number == g:
            return [number, result]
    return None
print(gap(8,300,400))
print(gap(2,100,110))
print(gap(10,300,400))