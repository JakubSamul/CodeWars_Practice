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
# s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa",
# "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
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


# String ends with?
# def solution(string, ending):
#     return string.endswith(ending)
# print(solution('abcde', 'cde'))


# Jaden Casing Strings
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


# Parts of a list
# def partlist(arr):
#     result = []
#     for e,i in enumerate(arr):
#         if e == len(arr)-1:
#             break
#         else:
#             result.append((" ".join(arr[:e+1]), " ".join(arr[e+1:])))
#     return result


# Even numbers in an array
# def even_numbers(arr,n):
#     result = []
#     for i in arr[::-1]:
#         if i % 2 == 0:
#             result.append(i)
#             if len(result) == n:
#                 break
#     return result[::-1]
# print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
# print(even_numbers([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2))


# Vowel Count
# def get_count(sentence):
#     num_vowels = 0
#     for vow in ["a", "e", "i", "o", "u"]:
#         num_vowels += sentence.count(vow)
#     return num_vowels


# Odd or Even?
# def odd_or_even(arr):
#     if sum(arr) % 2 == 0:
#         return "even"
#     else:
#         return "odd"


# Reverse words
# def reverse_words(text):
#     result = []
#     for word in text.split(" "):
#         result.append(word[::-1])
#     return " ".join(result)


# Greet Me
# def greet(name):
#     return 'Hello {}!'.format(name.title())


# Round up to the next multiple of 5
# def round_to_next5(n):
#     return n + (5 - n) % 5


# Factorial
# def factorial(n):
#     result = 1
#     if n < 0 or n > 12:
#         raise ValueError('Value Error')
#     else:
#         for i in range(1, n+1):
#             result *= i
#         return result


# Number of People in the Bus
# def number(bus_stops):
#     return sum([i[0] - i[1] for i in bus_stops])


# Shortest Word
# def find_short(s):
#     words = s.split(' ')
#     words.sort(key=len)
#     return len(words[0])


# Remove the minimum
# def remove_smallest(numbers):
#     new_list = numbers.copy()
#     if len(new_list) < 1 :
# 	    return numbers
#     else:
# 	    new_list.remove(min(new_list))
#     return new_list


# Deodorant Evaporator
# def evaporator(content, evap_per_day, threshold):
#     evap = evap_per_day / 100
#     content = 1
#     thres = threshold / 100
#     result = 0
#     while content > thres:
#         content = content * (1 - evap)
#         result += 1
#     return result


# Small enough? - Beginner
# def small_enough(array, limit):
#     to_much = 0
#     for i in array:
#         if i > limit:
#             to_much += 1
#     if to_much > 0 :
#         return False
#     else:
#         return True


# Anagram Detection
# # write the function is_anagram
# def is_anagram(test, original):
#     if sorted(test.lower()) != sorted(original.lower()):
#         return False
#     return True


# Find the vowels
# def vowel_indices(word):
#     word = word.lower()
#     num_vowels = []
#     c = 1
#     for i in range(0,len(word)):
#         if word[i] in ["a", "e", "i", "o", "u", "y"]:
#             num_vowels.append(c)
#         c += 1
#     return num_vowels


# Factorial
# def factorial(n):
#     total = 1
#     for num in range(1, n+1):
#         total = total * num
#     return total


# Moves in squared strings (I)
# s = "abcd\nefgh\nijkl\nmnop"

# def vert_mirror(strng):
#     result =[]
#     for i in strng.split('\n'):
#         result.append(i[::-1])
#     return '\n'.join(result)


# def hor_mirror(strng):
#     result =[]
#     for i in strng.split('\n'):
#         result.append(i)
#     return '\n'.join(result[::-1])

# def oper(fct, s):
#     return fct(s)

# # print(vert_mirror("hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"))
# # print(hor_mirror("hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"))
# print(oper(vert_mirror,s))


# Convert an array of strings to array of numbers
# def to_float_array(arr):
#     result = []
#     for number in arr:
#         result.append(float(number))
#     return result


# Sort the Gift Code
# def sort_gift_code(code):
#     code = list(code)
#     result = ""
#     for i in sorted(code):
#         result += i
#     return result


# Most digits
# a = [8, 900, 500, 891]
# def find_longest(arr):
#     sort_arr = sorted(arr)
#     l = len(str(sort_arr[-1]))
#     for i in arr:
#         if len(str(i)) == l:
#             return i
# print(find_longest(a))


# Fix string case
# a = 'asdKJHJKHKasdJKHKHKJH'
# def solve(s):
#     lower = 0
#     upper = 0
#     for i in s:
#         if i.isupper():
#             upper += 1
#         else:
#             lower +=1
#     if upper > lower:
#         return s.upper()
#     else:
#         return s.lower()
# print(solve(a))


# Summing a numbers digits
# def sum_digits(number):
#     sum = 0
#     for i in str(number):
#         if i == '-':
#             continue
#         sum += int(i)
#     return sum
# print(sum_digits(-111111))


# # Divide and Conquer
# def div_con(arr):
#     total_non_string = 0
#     total_string = 0

#     for item in arr:
#         if isinstance(item, int):
#             total_non_string += item
#         elif isinstance(item, str):
#             total_string += int(item)

#     return total_non_string - total_string
# a = ['5', '0', 9, 3, 2, 1, '9', 6, 7]
# print(div_con(a))


# Ordered Count of Characters
# def ordered_count(input_string):
#     char_counts = {}
#     for char in input_string:
#         if char in char_counts:
#             char_counts[char] += 1
#         else:
#             char_counts[char] = 1
#     char_count_tuples=[(char, count) for char, count in char_counts.items()]
#     return char_count_tuples


# Maximum Product
# def adjacent_element_product(array):
#     result = -1000000
#     for i in range(0, len(array) - 1):
#         multipling = array[i] * array[i + 1]
#         if multipling > result:
#             result = multipling
#     return result


# # Switcheroo
# def switcheroo(s):
#     string_list = list(s)
#     for i in range(len(s)):
#         if string_list[i] == 'a':
#             string_list[i] = 'b'
#         elif string_list[i] == 'b':
#             string_list[i] = 'a'
#     return ''.join(string_list)


# # Minimize Sum Of Array (Array Series #1)
# def min_sum(arr):
#     arr.sort(reverse=True)
#     result = 0
#     l = int(len(arr) / 2)
#     for i in range(1, l + 1):
#         result += arr[i - 1] * arr[-i]
#     return result


# # Spacify
# def spacify(string):
#     return " ".join(string)


# Nth Smallest Element (Array Series #4)
# def nth_smallest(arr, pos):
#     arr.sort()
#     return arr[pos - 1]


# Filter the number
# a = "abc1234"


# def filter_string(st):
#     result = ""
#     for i in st:
#         if i in "0123456789":
#             result += i
#     return int(result)


# print(filter_string(a))


# Power of two
# def power_of_two(x):
#     return x > 0 and (x & (x - 1)) == 0


# Sum of Cubes
# def sum_cubes(n):
#     return sum([i**3 for i in range(1, n + 1)])


# # Sum of numbers from 0 to N
# def show_sequence(n):
#     series = ""
#     total_sum = 0
#     if n == 0:
#         return "0=0"
#     if n < 0:
#         return f"{n}<0"
#     for i in range(n + 1):
#         total_sum += i
#         if i < n:
#             series += str(i) + "+"
#         else:
#             series += str(i)

#     series_with_sum = series + " = " + str(total_sum)
#     return series_with_sum


# Simple remove duplicate
# def solve(arr):
#     result = []
#     seen = set()
#     for item in reversed(arr):
#         if item not in seen:
#             result.append(item)
#             seen.add(item)
#     result.reverse()
#     return result


# Sum of Cubes
# def sum_cubes(n):
#     total_sum = 0
#     for i in range(1, n + 1):
#         total_sum += i**3
#     return total_sum


# The Coupon Code
from datetime import datetime


def check_coupon(enteredCode, correctCode, currentDate, expirationDate):
    current_date = datetime.strptime(currentDate, "%B %d, %Y")
    expiration_date = datetime.strptime(expirationDate, "%B %d, %Y")

    return enteredCode == correctCode and current_date <= expiration_date


# Test cases
print(check_coupon("123", "123", "July 9, 2015", "July 9, 2015"))
print(check_coupon("123", "123", "July 9, 2015", "July 2, 2015"))
