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