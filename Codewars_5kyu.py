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
a = "foobar23"
def increment_string(strng):
    result = strng.rstrip("0123456789")
    l = strng[len(result):]
    if l == "": 
        return strng+"1"
    else:
        return result + str(int(l) + 1).zfill(len(l))
print(increment_string(a))