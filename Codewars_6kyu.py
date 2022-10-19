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
# def encrypt(encrypted_text, n):
#     for i in str(n):
#         step1 = []
#         step2 = []
#         for step in range(1,len(encrypted_text)+1,2):
#             step1.append(encrypted_text[step])
#         for step in range(0,len(encrypted_text)+1,2):
#             step2 += encrypted_text[step]
#     print(step1)

# print(encrypt("This is a test!", 1))



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