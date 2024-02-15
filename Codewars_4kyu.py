# # Strings Mix
# a1 = "Sadus:cpms>orqn3zecwGvnznSgacs"
# a2 = "MynwdKizfd$lvse+gnbaGydxyXzayp"
# m1 = "Are they here"
# m2 = "yes, they are here"
# from collections import Counter

# def mix(a1, a2):
#     first = Counter(a1)
#     secound = Counter(a2)
#     result = []
#     for k, v in first.items():
#         if secound.get(k,0) == v:
#             result.append((k,v,3))
#         elif secound.get(k, 0) > v:
#             result.append((k, secound.pop(k),2))
#         else:
#             result.append((k,v,1))
#     for k, v in secound.items():
#         if k not in first:
#             result.append((k,v,2))
#     result = sorted(result, key = lambda x: (-x[1], x[2], x[0]))
#     data = ''
#     for k,v,i in result:
#         if v > 1 and k.isalpha() and k != k.upper():
#             data += f"{'=' if i == 3 else i}:{v*k}/"
#     if data:
#         data = data.strip('/')
#     return data
# print(mix(a1,a2))


# Snal 
def snail(snail_map):
    for i in range(0, len(snail_map)):

print(int(3/2))