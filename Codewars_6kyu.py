# # Title Case
# def title_case(title, minor_words=''):
#     result = ""
#     MinorWords = ""
#     for let in minor_words.split(" "):
#         let = let.lower()
#         MinorWords += let + " "
#     for leter in title.split(" "):
#         leter = leter.lower()
#         if leter in MinorWords:
#             result += leter + " "
#         else:
#             leter = leter.title()
#             result += leter + " "
#     result = result[0:len(result)-1]
#     first = result[0] if result else ""
#     return result.replace(first, first.upper(), 1)
# print(title_case('First a of in', ''))


# Simple Encryption #1 - Alternating Split
# def decrypt(text, n):
#     if n <= 0 or not text:
#         return text
#     text = list(text)
#     l = len(text)
#     for i in range(n):
#         text_a = list(text[0:l//2])
#         text_b = list(text[l//2:l])
#         for j in range(1,l,2):
#             k = text_a.pop(0)
#             text_b.insert(j,k)
#         text = text_b
#     return "".join(text_b)

# def encrypt(text, n):
#     if n <= 0:
#         return text
#     text = list(text)
#     for i in range(n):
#         step1 = []
#         step2 = []
#         for i in range(len(text)):
#             if i % 2 == 0:
#                 step2.append(text[i])
#             else:
#                 step1.append(text[i])
#         text = "".join(step1+step2)
#     return text
# print(encrypt("This is a test!", 1))
# print(decrypt("hsi  etTi sats!", 1))


# Help the bookseller !
# b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
# c = ["A", "B", "C", "D"]
# def stock_list(listOfArt, listOfCat):
#     final = ""
#     result = []
#     for i in range(len(listOfCat)):
#         result.append(listOfCat[i])
#         for j in range(len(result)):
#             result[j] = 0
#     for a in listOfArt:
#         a = a.split(" ")
#         cat = a[0]
#         for i in range(0,len(listOfCat)):
#             if cat[0] == listOfCat[i]:
#                 result[i] += int(a[1])
#     for c in range(len(result)):
#         final += "(" + listOfCat[c] + " : " + str(result[c]) + ") - "
#     if sum(result) == 0:
#         return ""
#     else:
#         return final[0:-3]
# print(stock_list(b,c))


# Find the odd int
# a = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
# def find_it(seq):
#     result = []
#     for i in range(len(seq)):
#         result.append(seq[i])
#         for j in range(len(result)):
#             result[j] = 0
#     for i in range(0,len(seq)):
#         for j in range(0,len(seq)):
#             if seq[i] == seq[j]:
#                 result[i] += 1
#     for i in result:
#         if i % 2 == 1:
#             a = result.index(i)
#             return seq[a]
# print(find_it(a))


# Count the smiley faces!
# a = [':)',':(',':D',':O',':;']
# b = [':D',':~)',';~D',':)']
# def count_smileys(arr):
#     count = 0
#     for i in arr:
#         if len(i) == 2:
#             if i[0] == ";" or i[0] == ":":
#                 if i[1] == ")" or i[1] == "D":
#                     count += 1
#         if len(i) == 3:
#             if i[0] == ";" or i[0] == ":":
#                 if i[1] == "-" or i[1] == "~":
#                     if i[2] == ")" or i[2] == "D":
#                         count += 1
#     return count
# print(count_smileys((b)))


# Break camelCase
# a = "asddKkokaoIijoaIklnk"
# def solution(s):
#     index = 0
#     result = []
#     for i in range(index,len(s)):
#         if s[i] == s[i].upper():
#             b = s[index:i]
#             result.append(b)
#             index = s.index(s[i],i-1,len(s))
#     result.append(s[index:len(s)])
#     return " ".join(result)
# print(solution(a))


# Build Tower
# def tower_builder(n_floors):
#     res = []
#     temp = ''
#     for i in range(n_floors):
#         temp = ''
#         for t in range(n_floors-i-1):
#             temp += ' '
#         print(temp)
#         for j in range(2*i+1):
#             temp += '*'
#         print(temp)
#         for k in range(n_floors-i-1):
#             temp += ' '
#         res.append(temp)
#     print(res)
#     return res
# print(tower_builder(6))


# Tortoise racing
# def race(v1, v2, g):
#     if v1 >= v2:
#         return None
#     else:
#         r = g * ( 3600 / ( v2 - v1 ))
#         s = int(r % 60)
#         m = int(r % 3600 / 60)
#         h = int(r / 3600)
#     return [h, m, s]
# print(race(720,850,70))


# Data Reverse
# data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
# data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
# def data_reverse(data):
#     result = []
#     s = []
#     final = []
#     for i in range(0,len(data)):
#         s.append(data[i])
#         if len(s) == 8:
#             result.append(s)
#             s = []
#     result = result[::-1]
#     for i in result:
#         for a in i:
#             final.append(a)
#     return final
# print(data_reverse(data1))


# Your order, please
# def order(sentence):
#     words = []
#     for i in range(1,10):
#         for word in sentence.split():
#             if str(i) in word:
#                 words.append(word)
#     return " ".join(words)


# The Vowel Code
# vow = {"a":"1", "e":"2", "i":"3", "o":"4", "u":"5"}
# def encode(st):
#     for w in vow:
#         st = st.replace(w, vow[w])
#     return st
# def decode(st):
#     for k,v in vow.items():
#         st = st.replace(v, k)
#     return st


# Replace With Alphabet Position
# def alphabet_position(text):
#     alp = "abcdefghijklmnopqrstuvwxyz"
#     return " ".join([str(alp.find(c) + 1) for c in text.lower() if c in alp])


# Duplicate Encoder
# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(x) == 1 else ")" for x in word.lower()])


# Consonant value
# import string
# def solve(s):
#     alpha_dict = {}
#     i = 0
#     for letter in string.ascii_lowercase:
#         i += 1
#         alpha_dict[letter] = i
#     list_word = []
#     temp =''
#     for letter in s:
#         if letter not in 'aeiou':
#             temp += letter
#         else:
#             list_word.append(temp)
#             temp = ''
#     if '' in list_word:
#         list_word.remove('')
#     word_value = []
#     for word in list_word:
#         temp = 0
#         for letter in word:
#             temp += alpha_dict[letter]
#         word_value.append(temp)
#     return max(word_value)


# Consecutive strings
# def longest_consec(strarr, k):
#     n = len(strarr)
#     if n == 0 or k > n or k <= 0:
#         return ''
#     longest = index = 0
#     for i in range(n - k + 1):
#         length = sum([len(s) for s in strarr[i: i + k]])
#         if length > longest:
#             longest = length
#             index = i
#     return ''.join(strarr[index: index + k])
# assert longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) == "abigailtheta"


# Count characters in your string
# def count(s):
#     return {c:s.count(c) for c in s}


# A Rule of Divisibility by 13
# def thirt(n):
#     pattern = [1, 10, 9, 12, 3, 4]
#     sum = 0

#     while True:
#         current_sum = 0
#         for index, digit in enumerate(str(n)[::-1]):
#             current_index = index % len(pattern)
#             current_sum += int(digit) * pattern[current_index]

#         if sum == current_sum:
#             return sum

#         sum = current_sum
#         n = current_sum


# Unique In Order
# def unique_in_order(sequence):
#     result = []
#     for i in sequence:
#         if len(result) < 1 or not i == result[len(result) - 1]:
#             result.append(i)
#     return result


# Highest Rank Number in an Array
# a = [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]
# def highest_rank(arr):
#     arr.sort()
#     arr1 = {}
#     for i in arr:
#         arr1[i] = 0
#     for j in arr:
#         same = 0
#         for k in arr:
#             if j == k:
#                 same += 1
#         arr1[j] = same
#     arr2 = sorted(arr1.items(), key = lambda x: x[1])
#     result = arr2[-1]
#     return result[0]

# print(highest_rank(a))


# Fibonacci, Tribonacci and friends
# a = [0, 1]
# def xbonacci(signature, n):
#     if n == 0:
#         return []
#     elif len(signature) >= n:
#         return signature[0:n]
#     else:
#         l = len(signature)
#         for i in range(0,n - len(signature)):
#             add = sum(signature[-l:])
#             signature.append(add)
#             print(signature)
#         return signature
# print(xbonacci(a, 10))


# Multiplication table
# def multiplication_table(size):
#     result = []
#     for i in range(1,size+1):
#         step = []
#         for j in range(1, size+1):
#             step.append(i*j)
#         result.append(step)
#     return result

# print(multiplication_table(3))


# # Bouncing Balls
# def bouncing_ball(h, bounce, window):
#     if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
#         return -1

#     passes = 0
#     while h > window:
#         passes += 1
#         h *= bounce
#         if h > window:
#             passes += 1

#     return passes


# # Reverse or rotate
# def rev_rot(str, sz):
#     if sz <= 0 or not str:
#         return ""
#     if sz > len(str):
#         return ""
#     modified_chunks = []
#     for i in range(0, len(str), sz):
#         chunk = str[i: i + sz]
#         if len(chunk) == sz:
#             digit_sum = sum(int(digit) ** 3 for digit in chunk)
#             if digit_sum % 2 == 0:
#                 modified_chunks.append(chunk[::-1])
#             else:
#                 modified_chunks.append(chunk[1:] + chunk[0])
#     return "".join(modified_chunks)


# # Dashatize it
# a = 1213212424


# def dashatize(n):
#     result = []
#     nn = str(abs(n))
#     for i in range(0, len(nn)):
#         if i == 0:
#             result.append(nn[i])
#             continue
#         if i == len(nn) - 1 and int(nn[i]) % 2 == 1:
#             result.append("-" + nn[i])
#             continue
#         if int(nn[i]) % 2 == 1 and int(nn[i - 1]) % 2 == 0:
#             result.append("-" + nn[i])
#             continue
#         if int(nn[i]) % 2 == 0 and int(nn[i - 1]) % 2 == 1:
#             result.append("-" + nn[i])
#             continue
#         if int(nn[i]) % 2 == 1 and int(nn[i - 1]) % 2 == 1:
#             result.append("-" + nn[i])
#             continue
#         if int(nn[i]) % 2 == 0:
#             result.append(nn[i])
#     return "".join(result)


# print(dashatize(a))


# Street Fighter 2 - Character Selection
# def street_fighter_selection(fighters, initial_position, moves):
#     rows, cols = len(fighters), len(fighters[0])
#     current_row, current_col = initial_position
#     selected_fighters = []

#     for move in moves:
#         if move == "up":
#             current_row = max(0, current_row - 1)
#         elif move == "down":
#             current_row = min(rows - 1, current_row + 1)
#         elif move == "left":
#             current_col = (current_col - 1) % cols
#         elif move == "right":
#             current_col = (current_col + 1) % cols

#         selected_fighters.append(fighters[current_row][current_col])

#     return selected_fighters


# Simple Encryption #1 - Alternating Split
# test = "This is a test!"
# test2 = "s eT ashi tist!"


# def decrypt(encrypted_text, n):
#     if encrypted_text == None:
#         return None
#     else:
#         result = encrypted_text
#         l = 0
#         if len(encrypted_text) % 2 == 1:
#             l = len(encrypted_text) - 1
#         else:
#             l = len(encrypted_text)
#         while n > 0:
#             w1 = ""
#             for i in range(int(l / 2), l):
#                 w1 += result[i]
#                 w1 += result[i - int((l / 2))]
#             if len(encrypted_text) % 2 == 1:
#                 w1 += result[-1]
#             result = w1
#             n -= 1
#         return result


# def encrypt(text, n):
#     result = text
#     while n > 0:
#         w1 = ""
#         for i in range(1, len(text), 2):
#             w1 += result[i]
#         for i in range(0, len(text), 2):
#             w1 += result[i]
#         result = w1
#         n -= 1
#     return result


# print(encrypt(test, 3))
# print(decrypt(test2, 2))


# # Replace With Alphabet Position
# def alphabet_position(text):
#     positions = []
#     for char in text:
#         if char.isalpha():
#             position = ord(char.lower()) - ord("a") + 1
#             positions.append(str(position))
#     return " ".join(positions)


# Meeting
# def meeting(s):
#     names = s.upper().split(";")

#     sorted_names = sorted(names, key=lambda x: (x.split(":")[1], x.split(":")[0]))

#     formatted_names = ""
#     for name in sorted_names:
#         first_name, last_name = name.split(":")
#         formatted_names += f"({last_name}, {first_name})"

#     return formatted_names


# # Prime ant
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True


# def prime_ant(n):
#     A = [i for i in range(2, 2 * n + 1)]  # Initialize array/list A
#     p = 0  # Initial position of the ant
#     for _ in range(n):
#         if is_prime(A[p]):
#             p += 1
#         else:
#             q = 2  # Smallest divisor greater than 1
#             while A[p] % q != 0 or not is_prime(q):
#                 q += 1
#             A[p] //= q
#             A[p - 1] += q
#             p -= 1
#     return p


# print(prime_ant(11))


# Break camelCase
# def solution(s):
#     result = ""
#     for char in s:
#         if char.isupper():
#             result += " " + char
#         else:
#             result += char
#     return result


# print(solution("camelCasing"))
# print(solution("identifier"))
# print(solution(""))


# Highest Rank Number in an Array
# def highest_rank(arr: list) -> int:
#     arr1 = set(arr)
#     repetitionDict = {}
#     for number in arr1:
#         repeating = 0
#         for _ in arr:
#             if number == _:
#                 repeating += 1
#         repetitionDict[number] = repeating
#     maxRepetition = max(repetitionDict.values())
#     mostRepetition = [k for k, v in repetitionDict.items() if v == maxRepetition]
#     return max(mostRepetition)


# f = [12, 10, 8, 12, 7, 6, 4, 10, 12]
# s = [12, 10, 8, 12, 7, 6, 4, 10, 10]
# t = [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]

# print(highest_rank(f))
# print(highest_rank(s))
# print(highest_rank(t))


# Two Sum
# def two_sum(nums, target):
#     num_dict = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_dict:
#             return (num_dict[complement], i)
#         num_dict[num] = i


# print(two_sum([1, 2, 3], 4))
# print(two_sum([3, 2, 4], 6))


# Count characters in your string
def count(s):
    if not s:
        return {}

    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


print(count("aba"))
print(count(""))
