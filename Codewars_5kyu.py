# # Sum of Pairs
# def sum_pairs(ints, s):
#     result = []
#     lenght = len(ints)
#     for a in ints[:lenght-1]:
#         step = 1
#         for b in ints[step+1:]:
#             if a + b == s:
#                 if result == []:
#                     result.append(a)
#                     result.append(b)
#                 else:
#                     c = result[1]
#                     if ints.index(b) < ints.index(c):
#                         result[0] = a
#                         result[1] = b
#         step += 1
#     if result == []:
#         return None
#     else:
#         return result



# Directions Reduction
a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
def dirReduc(arr):
    for a in arr:
        for b in arr[1:]:
            if a == "NORTH" and b == "SOUTH":
                del arr[arr.index(a)]
                del arr[arr.index(b)]
            elif a == "SOUTH" and b == "NORTH":
                del arr[arr.index(a)]
                del arr[arr.index(b)]
            elif a == "WEST" and b == "EAST":
                del arr[arr.index(a)]
                del arr[arr.index(b)]
            elif a == "EAST" and b == "WEST":
                del arr[arr.index(a)]
                del arr[arr.index(b)]
    return arr
print(dirReduc(a))