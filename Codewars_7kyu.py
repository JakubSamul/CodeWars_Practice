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



# Row Weights
# def row_weights(array):
#     if len(array) == 1:
#         return (array[0],0)
#     elif len(array) == 2:
#         return (array[0], array[1])
#     else:
#         res1 = 0
#         res2 = 0
#         for i in range(0,len(array),2):
#             res1 += array[i]
#         for i in range(1,len(array),2):
#             res2 += array[i]
#         return (res1,res2)
# print(row_weights([29,83,67,53,19,28,96]))



#String ends with?
# def solution(string, ending):
#     return string.endswith(ending)
# print(solution('abcde', 'cde'))



#Jaden Casing Strings
# a = "How can mirrors be real if our eyes aren't real"
# def to_jaden_case(string):
#     result = ''
#     string1 = string.split()
#     for i in string1:
#         result += i.capitalize() + ' '
#     return result[0:-1]
# print(to_jaden_case(a))



# Sum of angles
# def angle(n):
#     if n >= 3:
#         return (n-2) * 180
# print(angle(4))



# Sum of old numbers
# def row_sum_odd_numbers(n):
#     n1 = n * (n-1) + 1
#     result = 0
#     result += n1
#     for i in range(1,n):
#         n2 = n1 + i * 2
#         result += n2
#     return result
# print(row_sum_odd_numbers(13))



# Sorted? yes? no? how?
# def is_sorted_and_how(arr):
#     if arr == sorted(arr):
#         return 'yes, ascending'
#     elif arr == sorted(arr)[::-1]:
#         return 'yes, descending'
#     else:
#         return 'no'
# print(is_sorted_and_how([9,6,4,3,1,0]))



# Bumps in the Road
# def bumps(road):
#     result = 0
#     for i in range(0,len(road)):
#         if road[i] == "n":
#             result += 1
#     if result > 15:
#         return 'Car Dead'
#     else:
#         return "Woohoo!"
# print(bumps("_nnnnnnn_n__n______nn__nn_nnn"))



# JavaScript Array Filter
# def get_even_numbers(arr):
#     return list(filter(lambda x: x%2 == 0, arr)) 



# Flatten and sort an array
# def flatten_and_sort(array):
# 	result=[]
# 	for a in array:
# 		for x in a:
# 			result.append(x)
# 	return sorted(result)



# No oddities here
# def no_odds(values):
#     return [value for value in values if value % 2 == 0]